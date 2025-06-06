# UIPickerViewDataSource

**Framework**: UIKit  
**Kind**: protocol

The interface for a picker view’s data source.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIPickerViewDataSource : NSObjectProtocol
```

#### Overview

The data source of a [`UIPickerView`](uipickerview.md) object must adopt this protocol to mediate between the picker view object and your app’s data model for that picker view. The data source provides the picker view with the number of components, and the number of rows in each component, for displaying the picker view data. Both methods in this protocol are required.

## Topics

### Providing counts for the picker view
- [func numberOfComponents(in: UIPickerView) -> Int](uipickerviewdatasource/numberofcomponents(in:).md)
  Asks the data source for the number of components in the picker view.
- [func pickerView(UIPickerView, numberOfRowsInComponent: Int) -> Int](uipickerviewdatasource/pickerview(_:numberofrowsincomponent:).md)
  Asks the data source for the number of rows for a specified component.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var dataSource: (any UIPickerViewDataSource)?](uipickerview/datasource.md)
  The data source for the picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdatasource)*