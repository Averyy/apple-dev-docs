# numberOfComponents

**Framework**: UIKit  
**Kind**: property

The number of components for the picker view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var numberOfComponents: Int { get }
```

#### Discussion

A [`UIPickerView`](uipickerview.md) object fetches the value of this property from the data source and caches it. The default value is `0`.

## See Also

- [func numberOfRows(inComponent: Int) -> Int](uipickerview/numberofrows(incomponent:).md)
  Returns the number of rows for a component.
- [func rowSize(forComponent: Int) -> CGSize](uipickerview/rowsize(forcomponent:).md)
  Returns the size of a row for a component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/numberofcomponents)*