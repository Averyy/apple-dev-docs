# numberOfRows(inComponent:)

**Framework**: UIKit  
**Kind**: method

Returns the number of rows for a component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func numberOfRows(inComponent component: Int) -> Int
```

#### Return Value

The number of rows in the given component.

#### Discussion

A picker view fetches the value of this property from the data source and and caches it. The default value is zero.

## Parameters

- `component`: A zero-indexed number identifying a component.

## See Also

- [var numberOfComponents: Int](uipickerview/numberofcomponents.md)
  The number of components for the picker view.
- [func rowSize(forComponent: Int) -> CGSize](uipickerview/rowsize(forcomponent:).md)
  Returns the size of a row for a component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/numberofrows(incomponent:))*