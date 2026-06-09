# matchedTransitionSource(id:in:)

**Framework**: SwiftUI  
**Kind**: method

Identifies this view as the source of a navigation transition, such as a zoom transition.

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
nonisolated
func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID) -> some View
```

## Parameters

- `id`: The identifier, often derived from the identifier of the data being displayed by the view.
- `namespace`: The namespace in which defines the `id`. New namespaces are created by adding an [`Namespace`](namespace.md) variable to a [`View`](view.md) type and reading its value in the view’s body method.

## See Also

- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](view/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [protocol MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration.md)
  A configuration that defines the appearance of a matched transition source.
- [struct EmptyMatchedTransitionSourceConfiguration](emptymatchedtransitionsourceconfiguration.md)
  An unstyled matched transition source configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/matchedtransitionsource(id:in:))*