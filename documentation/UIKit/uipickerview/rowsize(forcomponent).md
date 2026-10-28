# rowSize(forComponent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the size of a row for a component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func rowSize(forComponent component: Int) -> CGSize
```

```objc
- (CGSize) rowSizeForComponent:(NSInteger) component;
```

## Return Value

The size of rows in the given component. This is generally the size required to display the largest string or view used as a row in the component.

## Discussion

A picker view fetches the value of this property by calling the [`pickerView(_:widthForComponent:)`](../uipickerviewdelegate/pickerview%28_,widthforcomponent%29.md) and [`pickerView(_:rowHeightForComponent:)`](../uipickerviewdelegate/pickerview%28_,rowheightforcomponent%29.md) delegate methods, and caches it. The default value is (`0`, `0`).

## Parameters

- `component`: A zero-indexed number identifying a component.

## See Also

### Getting the dimensions of the picker view
- [var numberOfComponents: Int](./numberofcomponents.md)
  The number of components for the picker view.
- [func numberOfRows(inComponent: Int) -> Int](./numberofrows%28incomponent%29.md)
  Returns the number of rows for a component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/rowsize(forcomponent:))*