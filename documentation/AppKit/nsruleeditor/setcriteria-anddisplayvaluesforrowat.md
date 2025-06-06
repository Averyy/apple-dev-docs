# setCriteria(_:andDisplayValues:forRowAt:)

**Framework**: AppKit  
**Kind**: method

Modifies the row at a given index to contain the given items and values.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setCriteria(_ criteria: [Any], andDisplayValues values: [Any], forRowAt rowIndex: Int)
```

#### Discussion

It is your responsibility to ensure that each item in the array is a child of the previous item, and that the first item is a root item for the row type. If the last item has child items, then the items array will be extended by querying the delegate for child items until a childless item is reached. If `values` contains fewer objects than the (possibly extended) criteria array, then the delegate is queried to construct the remaining display values. If you want the delegate to be queried for all the criteria or all the display values, pass empty arrays; do not pass `nil`.

## Parameters

- `criteria`: The array of criteria for the row at  . Pass an empty array to force the receiver to query its delegate. This value must not be  .
- `values`: The array of values for the row at  . Pass an empty array to force the receiver to query its delegate. This value must not be  .
- `rowIndex`: The index of a row in the receiver.

## See Also

- [func reloadCriteria()](nsruleeditor/reloadcriteria.md)
  Instructs the receiver to refetch criteria from its delegate.
- [func criteria(forRow: Int) -> [Any]](nsruleeditor/criteria(forrow:).md)
  Returns the currently chosen items for a given row.
- [func displayValues(forRow: Int) -> [Any]](nsruleeditor/displayvalues(forrow:).md)
  Returns the chosen values for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/setcriteria(_:anddisplayvalues:forrowat:))*