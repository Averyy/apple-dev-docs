# ZoomNavigationTransition

**Framework**: SwiftUI  
**Kind**: struct

A navigation transition that zooms the appearing view from a given source view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ZoomNavigationTransition
```

#### Overview

Indicate the source view using the [`matchedTransitionSource(id:in:)`](view/matchedtransitionsource(id:in:).md) modifier.

> **Note**: The zoom transition is not supported in tvOS. Navigation uses [`automatic`](navigationtransition/automatic.md) instead.

## Relationships

### Conforms To
- [NavigationTransition](navigationtransition.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/zoomnavigationtransition)*