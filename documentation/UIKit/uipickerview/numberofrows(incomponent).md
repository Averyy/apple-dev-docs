# numberOfRows(inComponent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of rows for a component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func numberOfRows(inComponent component: Int) -> Int
```

```objc
- (NSInteger) numberOfRowsInComponent:(NSInteger) component;
```

## Return Value

The number of rows in the given component.

## Discussion

A picker view fetches the value of this property from the data source and and caches it. The default value is zero.

## Parameters

- `component`: A zero-indexed number identifying a component.

## See Also

### Getting the dimensions of the picker view
- [var numberOfComponents: Int](./numberofcomponents.md)
  The number of components for the picker view.
- [func rowSize(forComponent: Int) -> CGSize](./rowsize%28forcomponent%29.md)
  Returns the size of a row for a component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/numberofrows(incomponent:))*