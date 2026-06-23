# zoom(sourceID:in:)

**Framework**: SwiftUI  
**Kind**: method

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
static func zoom(sourceID: some Hashable, in namespace: Namespace.ID) -> ZoomNavigationTransition
```

#### Discussion

Indicate the source view using the [`matchedTransitionSource(id:in:)`](view/matchedtransitionsource(id:in:).md) modifier.

> **Note**: The zoom transition is not supported in tvOS. Navigation uses [`automatic`](navigationtransition/automatic.md) instead.

## Parameters

- `sourceID`: The identifier you provide to a corresponding `matchedTransitionSource` modifier.
- `namespace`: The namespace where you define the `id`. You can create new namespaces by adding the [`Namespace`](namespace.md) attribute to a [`View`](view.md) type, then reading its value in the view’s body method.

## See Also

- [static var automatic: AutomaticNavigationTransition](navigationtransition/automatic.md)
  A style that automatically chooses the appropriate presentation transition for the current context.
- [struct AutomaticNavigationTransition](automaticnavigationtransition.md)
  A style that automatically chooses the appropriate presentation transition for the current context.
- [static var crossFade: CrossFadeNavigationTransition](navigationtransition/crossfade.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.
- [struct CrossFadeNavigationTransition](crossfadenavigationtransition.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.
- [struct ZoomNavigationTransition](zoomnavigationtransition.md)
  A navigation transition that zooms the appearing view from a given source view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationtransition/zoom(sourceid:in:))*