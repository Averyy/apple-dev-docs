# NavigationTransition

**Framework**: SwiftUI  
**Kind**: protocol

A type that defines the transition to use when navigating to a view.

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
protocol NavigationTransition
```

## Topics

### Getting built-in transitions
- [static var automatic: AutomaticNavigationTransition](navigationtransition/automatic.md)
  A style that automatically chooses the appropriate presentation transition for the current context.
- [struct AutomaticNavigationTransition](automaticnavigationtransition.md)
  A style that automatically chooses the appropriate presentation transition for the current context.
- [static var crossFade: CrossFadeNavigationTransition](navigationtransition/crossfade.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.
- [struct CrossFadeNavigationTransition](crossfadenavigationtransition.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.
- [static func zoom(sourceID: some Hashable, in: Namespace.ID) -> ZoomNavigationTransition](navigationtransition/zoom(sourceid:in:).md)
  A navigation transition that zooms the appearing view from a given source view.
- [struct ZoomNavigationTransition](zoomnavigationtransition.md)
  A navigation transition that zooms the appearing view from a given source view.

## Relationships

### Conforming Types
- [AnyNavigationTransition](anynavigationtransition.md)
- [AutomaticNavigationTransition](automaticnavigationtransition.md)
- [CrossFadeNavigationTransition](crossfadenavigationtransition.md)
- [ZoomNavigationTransition](zoomnavigationtransition.md)

## See Also

- [func navigationTransition(some NavigationTransition) -> some View](view/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [struct AnyNavigationTransition](anynavigationtransition.md)
  A type-erasing navigation transition that allows for providing any navigation transition value dynamically.
- [struct CrossFadeNavigationTransition](crossfadenavigationtransition.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationtransition)*