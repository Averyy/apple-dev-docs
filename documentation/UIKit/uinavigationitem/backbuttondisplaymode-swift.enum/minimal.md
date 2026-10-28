# UINavigationItem.BackButtonDisplayMode.minimal

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The navigation item displays the Back button indicator instead of a title.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
case minimal
```

```c
UINavigationItemBackButtonDisplayModeMinimal
```

## Discussion

When you set the [`backButtonDisplayMode`](../backbuttondisplaymode-swift.property.md) property to this value, the Back button doesn’t display a title. Instead, it displays the Back button indicator image.

## See Also

### Constants
- [UINavigationItem.BackButtonDisplayMode.default](./default.md)
  The navigation item attempts to display a specific title, a generic title, or no title for the Back button, depending on the space available.
- [UINavigationItem.BackButtonDisplayMode.generic](./generic.md)
  The navigation item attempts to display a generic title or no title for the Back button, depending on the space available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum/minimal)*