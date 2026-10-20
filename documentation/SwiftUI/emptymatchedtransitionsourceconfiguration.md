# EmptyMatchedTransitionSourceConfiguration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [MatchedTransitionSourceConfiguration](./matchedtransitionsourceconfiguration.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining matched transitions
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](./view/matchedtransitionsource%28id,in%29.md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](./view/matchedtransitionsource%28id,in,configuration%29.md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [protocol MatchedTransitionSourceConfiguration](./matchedtransitionsourceconfiguration.md)
  A configuration that defines the appearance of a matched transition source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptymatchedtransitionsourceconfiguration)*