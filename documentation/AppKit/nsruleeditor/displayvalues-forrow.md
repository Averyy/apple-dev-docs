# displayValues(forRow:)

**Framework**: AppKit  
**Kind**: method

Returns the chosen values for a given row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func displayValues(forRow row: Int) -> [Any]
```

#### Return Value

The chosen values (strings, views, or menu items) for row `row`.

#### Discussion

The values returned are the same as those returned from the delegate’s [`ruleEditor(_:displayValueForCriterion:inRow:)`](nsruleeditordelegate/ruleeditor(_:displayvalueforcriterion:inrow:).md) method.

## Parameters

- `row`: The index of a row in the receiver.

## See Also

- [func reloadCriteria()](nsruleeditor/reloadcriteria.md)
  Instructs the receiver to refetch criteria from its delegate.
- [func setCriteria([Any], andDisplayValues: [Any], forRowAt: Int)](nsruleeditor/setcriteria(_:anddisplayvalues:forrowat:).md)
  Modifies the row at a given index to contain the given items and values.
- [func criteria(forRow: Int) -> [Any]](nsruleeditor/criteria(forrow:).md)
  Returns the currently chosen items for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/displayvalues(forrow:))*