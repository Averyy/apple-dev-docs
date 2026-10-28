# pickerView(_:numberOfRowsInComponent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the data source for the number of rows for a specified component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int
```

```objc
- (NSInteger) pickerView:(UIPickerView *) pickerView numberOfRowsInComponent:(NSInteger) component;
```

## Return Value

The number of rows for the component.

## Parameters

- `pickerView`: The picker view requesting the data.
- `component`: A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.

## See Also

### Providing counts for the picker view
- [func numberOfComponents(in: UIPickerView) -> Int](./numberofcomponents%28in%29.md)
  Asks the data source for the number of components in the picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdatasource/pickerview(_:numberofrowsincomponent:))*