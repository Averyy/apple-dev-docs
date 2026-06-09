# EmptyMatchedTransitionSourceConfiguration

**Framework**: SwiftUI  
**Kind**: struct

An unstyled matched transition source configuration.

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
struct EmptyMatchedTransitionSourceConfiguration
```

## Relationships

### Conforms To
- [MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](view/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](view/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [protocol MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration.md)
  A configuration that defines the appearance of a matched transition source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptymatchedtransitionsourceconfiguration)*