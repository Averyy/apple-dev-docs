# dataSource

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The data source for the picker view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var dataSource: (any UIPickerViewDataSource)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIPickerViewDataSource> dataSource;
```

#### Discussion

The data source must adopt the [`UIPickerViewDataSource`](../uipickerviewdatasource.md) protocol and implement the required methods to return the number of components and the number of rows in each component.

## See Also

### Providing the picker data
- [protocol UIPickerViewDataSource](../uipickerviewdatasource.md)
  The interface for a picker view’s data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/datasource)*