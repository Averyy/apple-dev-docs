# pickerView(_:numberOfRowsInComponent:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the data source for the number of rows for a specified component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int
```

#### Return Value

The number of rows for the component.

## Parameters

- `pickerView`: The picker view requesting the data.
- `component`: A zero-indexed number identifying a component of  . Components are numbered left-to-right.

## See Also

- [func numberOfComponents(in: UIPickerView) -> Int](uipickerviewdatasource/numberofcomponents(in:).md)
  Asks the data source for the number of components in the picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdatasource/pickerview(_:numberofrowsincomponent:))*