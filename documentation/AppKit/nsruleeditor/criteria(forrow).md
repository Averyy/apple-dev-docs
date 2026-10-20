# criteria(forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the currently chosen items for a given row.

**Availability**:
- macOS

## Declaration

```swift
func criteria(forRow row: Int) -> [Any]
```

```objc
- (NSArray *) criteriaForRow:(NSInteger) row;
```

#### Return Value

The currently chosen items for row `row`.

#### Discussion

The items returned are the same as those returned by calling the delegate’s [`ruleEditor(_:child:forCriterion:with:)`](../nsruleeditordelegate/ruleeditor%28_,child,forcriterion,with%29.md) method once for each item in the row.

## Parameters

- `row`: The index of a row in the receiver.

## See Also

### Providing Data
- [func reloadCriteria()](./reloadcriteria%28%29.md)
  Instructs the receiver to refetch criteria from its delegate.
- [func setCriteria([Any], andDisplayValues: [Any], forRowAt: Int)](./setcriteria%28_,anddisplayvalues,forrowat%29.md)
  Modifies the row at a given index to contain the given items and values.
- [func displayValues(forRow: Int) -> [Any]](./displayvalues%28forrow%29.md)
  Returns the chosen values for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/criteria(forrow:))*