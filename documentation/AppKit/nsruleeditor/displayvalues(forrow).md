# displayValues(forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the chosen values for a given row.

**Availability**:
- macOS

## Declaration

```swift
func displayValues(forRow row: Int) -> [Any]
```

```objc
- (NSArray *) displayValuesForRow:(NSInteger) row;
```

## Return Value

The chosen values (strings, views, or menu items) for row `row`.

## Discussion

The values returned are the same as those returned from the delegate’s [`ruleEditor(_:displayValueForCriterion:inRow:)`](../nsruleeditordelegate/ruleeditor%28_,displayvalueforcriterion,inrow%29.md) method.

## Parameters

- `row`: The index of a row in the receiver.

## See Also

### Providing Data
- [func reloadCriteria()](./reloadcriteria%28%29.md)
  Instructs the receiver to refetch criteria from its delegate.
- [func setCriteria([Any], andDisplayValues: [Any], forRowAt: Int)](./setcriteria%28_,anddisplayvalues,forrowat%29.md)
  Modifies the row at a given index to contain the given items and values.
- [func criteria(forRow: Int) -> [Any]](./criteria%28forrow%29.md)
  Returns the currently chosen items for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/displayvalues(forrow:))*