# numberOfComponents

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number of components for the picker view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var numberOfComponents: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger numberOfComponents;
```

#### Discussion

A [`UIPickerView`](../uipickerview.md) object fetches the value of this property from the data source and caches it. The default value is `0`.

## See Also

### Getting the dimensions of the picker view
- [func numberOfRows(inComponent: Int) -> Int](./numberofrows%28incomponent%29.md)
  Returns the number of rows for a component.
- [func rowSize(forComponent: Int) -> CGSize](./rowsize%28forcomponent%29.md)
  Returns the size of a row for a component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/numberofcomponents)*