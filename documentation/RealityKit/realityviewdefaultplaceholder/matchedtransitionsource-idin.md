# matchedTransitionSource(id:in:)

**Framework**: RealityKit  
**Kind**: method

Identifies this view as the source of a navigation transition, such as a zoom transition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID) -> some View
```

## Parameters

- `id`: The identifier, often derived from the identifier of   the data being displayed by the view.
- `namespace`: The namespace in which defines the  . New   namespaces are created by adding an   variable   to a   type and reading its value in the view’s body   method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/matchedtransitionsource(id:in:))*