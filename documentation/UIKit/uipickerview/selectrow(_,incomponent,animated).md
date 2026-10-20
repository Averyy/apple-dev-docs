# selectRow(_:inComponent:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Selects a row in a specified component of the picker view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func selectRow(_ row: Int, inComponent component: Int, animated: Bool)
```

```objc
- (void) selectRow:(NSInteger) row inComponent:(NSInteger) component animated:(BOOL) animated;
```

## Parameters

- `row`: A zero-indexed number identifying a row of `component`.
- `component`: A zero-indexed number identifying a component of the picker view.
- `animated`: [`true`](../../Swift/true.md) to animate the selection by spinning the wheel (component) to the new value; if you specify [`false`](../../Swift/false.md), the new selection is shown immediately.

## See Also

### Selecting rows in the view picker
- [func selectedRow(inComponent: Int) -> Int](./selectedrow%28incomponent%29.md)
  Returns the index of the selected row in a given component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/selectrow(_:incomponent:animated:))*