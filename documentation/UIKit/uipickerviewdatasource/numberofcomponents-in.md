# numberOfComponents(in:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the data source for the number of components in the picker view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func numberOfComponents(in pickerView: UIPickerView) -> Int
```

#### Return Value

The number of components (or “columns”) that the picker view should display.

## Parameters

- `pickerView`: The picker view requesting the data.

## See Also

- [func pickerView(UIPickerView, numberOfRowsInComponent: Int) -> Int](uipickerviewdatasource/pickerview(_:numberofrowsincomponent:).md)
  Asks the data source for the number of rows for a specified component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdatasource/numberofcomponents(in:))*