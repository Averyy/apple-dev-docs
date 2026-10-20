# Edge.Corner.Set

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An efficient set of corners.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Set
```

## Topics

### Initializers
- [init(Edge.Corner)](./set/init%28_%29.md)
  Creates set of corners containing only the specified corner.
- [init(rawValue: Int8)](./set/init%28rawvalue%29.md)
  Creates a corner set given a raw value.
### Instance Methods
- [func contains(Edge.Corner) -> Bool](./set/contains%28_%29.md)
  Returns true only if `corner` is a member of the calling set.
### Type Properties
- [static let all: Edge.Corner.Set](./set/all.md)
  All corners.
- [static let bottom: Edge.Corner.Set](./set/bottom.md)
  The bottom leading and trailing corners.
- [static let bottomLeading: Edge.Corner.Set](./set/bottomleading.md)
  The bottom leading corner.
- [static let bottomTrailing: Edge.Corner.Set](./set/bottomtrailing.md)
  The bottom trailing corner.
- [static let leading: Edge.Corner.Set](./set/leading.md)
  The top and bottom leading corners.
- [static let none: Edge.Corner.Set](./set/none.md)
  No corners.
- [static let top: Edge.Corner.Set](./set/top.md)
  The top leading and trailing corners.
- [static let topLeading: Edge.Corner.Set](./set/topleading.md)
  The top leading corner.
- [static let topTrailing: Edge.Corner.Set](./set/toptrailing.md)
  The top trailing corner.
- [static let trailing: Edge.Corner.Set](./set/trailing.md)
  The top and bottom trailing corners.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../../Swift/hashable.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge/corner/set)*