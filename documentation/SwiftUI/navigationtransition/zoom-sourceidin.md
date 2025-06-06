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

Indicate the source view using the `View/matchedTransitionSource(id:namespace:)` modifier.

## Parameters

- `sourceID`: The identifier you provide to a corresponding    modifier.
- `namespace`: The namespace where you define the  . You can create   new namespaces by adding the   attribute   to a   type, then reading its value in the view’s body   method.

## See Also

- [static var automatic: AutomaticNavigationTransition](navigationtransition/automatic.md)
  A style that automatically chooses the appropriate presentation transition for the current context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationtransition/zoom(sourceid:in:))*