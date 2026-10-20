# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A style that automatically chooses the appropriate presentation transition for the current context.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static var automatic: AutomaticNavigationTransition { get }
```

Available when `Self` is `AutomaticNavigationTransition`.

## See Also

### Getting built-in transitions
- [struct AutomaticNavigationTransition](../automaticnavigationtransition.md)
  A style that automatically chooses the appropriate presentation transition for the current context.
- [static var crossFade: CrossFadeNavigationTransition](./crossfade.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.
- [struct CrossFadeNavigationTransition](../crossfadenavigationtransition.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.
- [static func zoom(sourceID: some Hashable, in: Namespace.ID) -> ZoomNavigationTransition](./zoom%28sourceid,in%29.md)
  A navigation transition that zooms the appearing view from a given source view.
- [struct ZoomNavigationTransition](../zoomnavigationtransition.md)
  A navigation transition that zooms the appearing view from a given source view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationtransition/automatic)*