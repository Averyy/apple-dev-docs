# UINavigationItem.BackButtonDisplayMode.default

**Framework**: UIKit  
**Kind**: case

The navigation item attempts to display a specific title, a generic title, or no title for the Back button, depending on the space available.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case `default`
```

#### Discussion

When you set the [`backButtonDisplayMode`](uinavigationitem/backbuttondisplaymode-swift.property.md) property to this value, the navigation item attempts to display these titles for its Back button in the following order:

- [`backButtonTitle`](uinavigationitem/backbuttontitle.md)
- [`title`](uinavigationitem/title.md)
- A generic title, such as 
- No title

The navigation item selects the most appropriate title for the Back button according to the available space.

## See Also

- [UINavigationItem.BackButtonDisplayMode.generic](uinavigationitem/backbuttondisplaymode-swift.enum/generic.md)
  The navigation item attempts to display a generic title or no title for the Back button, depending on the space available.
- [UINavigationItem.BackButtonDisplayMode.minimal](uinavigationitem/backbuttondisplaymode-swift.enum/minimal.md)
  The navigation item displays the Back button indicator instead of a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum/default)*