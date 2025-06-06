# position(for:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the position of the specified bar in its new window.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func position(for bar: any UIBarPositioning) -> UIBarPosition
```

#### Return Value

The position of the bar.

#### Discussion

If your interface has a custom bar with a delegate, that delegate can implement this method and use it to specify the position of the bar that has been added to a window.

Delegates for the [`UINavigationBar`](uinavigationbar.md) and [`UISearchBar`](uisearchbar.md) classes return the value [`UIBarPosition.top`](uibarposition/top.md) by default. The delegate of the [`UIToolbar`](uitoolbar.md) class returns the value [`UIBarPosition.bottom`](uibarposition/bottom.md) by default.

## Parameters

- `bar`: The bar that was added to the window.

## See Also

- [protocol UIBarPositioning](uibarpositioning.md)
  A set of methods for defining the positioning of bars in iOS apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarpositioningdelegate/position(for:))*