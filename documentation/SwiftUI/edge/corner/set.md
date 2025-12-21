# Edge.Corner.Set

**Framework**: SwiftUI  
**Kind**: struct

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
- [init(Edge.Corner)](edge/corner/set/init(_:).md)
  Creates set of corners containing only the specified corner.
- [init(rawValue: Int8)](edge/corner/set/init(rawvalue:).md)
  Creates a corner set given a raw value.
### Instance Methods
- [func contains(Edge.Corner) -> Bool](edge/corner/set/contains(_:).md)
  Returns true only if `corner` is a member of the calling set.
### Type Properties
- [static let all: Edge.Corner.Set](edge/corner/set/all.md)
  All corners.
- [static let bottom: Edge.Corner.Set](edge/corner/set/bottom.md)
  The bottom leading and trailing corners.
- [static let bottomLeading: Edge.Corner.Set](edge/corner/set/bottomleading.md)
  The bottom leading corner.
- [static let bottomTrailing: Edge.Corner.Set](edge/corner/set/bottomtrailing.md)
  The bottom trailing corner.
- [static let leading: Edge.Corner.Set](edge/corner/set/leading.md)
  The top and bottom leading corners.
- [static let none: Edge.Corner.Set](edge/corner/set/none.md)
  No corners.
- [static let top: Edge.Corner.Set](edge/corner/set/top.md)
  The top leading and trailing corners.
- [static let topLeading: Edge.Corner.Set](edge/corner/set/topleading.md)
  The top leading corner.
- [static let topTrailing: Edge.Corner.Set](edge/corner/set/toptrailing.md)
  The top trailing corner.
- [static let trailing: Edge.Corner.Set](edge/corner/set/trailing.md)
  The top and bottom trailing corners.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge/corner/set)*