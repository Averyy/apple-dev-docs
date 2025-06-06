# criteria(forRow:)

**Framework**: AppKit  
**Kind**: method

Returns the currently chosen items for a given row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func criteria(forRow row: Int) -> [Any]
```

#### Return Value

The currently chosen items for row `row`.

#### Discussion

The items returned are the same as those returned by calling the delegate’s [`ruleEditor(_:child:forCriterion:with:)`](nsruleeditordelegate/ruleeditor(_:child:forcriterion:with:).md) method once for each item in the row.

## Parameters

- `row`: The index of a row in the receiver.

## See Also

- [func reloadCriteria()](nsruleeditor/reloadcriteria.md)
  Instructs the receiver to refetch criteria from its delegate.
- [func setCriteria([Any], andDisplayValues: [Any], forRowAt: Int)](nsruleeditor/setcriteria(_:anddisplayvalues:forrowat:).md)
  Modifies the row at a given index to contain the given items and values.
- [func displayValues(forRow: Int) -> [Any]](nsruleeditor/displayvalues(forrow:).md)
  Returns the chosen values for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/criteria(forrow:))*