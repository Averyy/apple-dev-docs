# kind

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The kind of the region.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
var kind: ReservedRegion.Kind { get }
```

#### Discussion

The kind tells you how to respond to the region. Place your content outside an [`occlusion`](./kind-swift.struct/occlusion.md) region, and arrange it on both sides of a [`division`](./kind-swift.struct/division.md) region.

## See Also

### Getting the region’s identity and kind
- [var id: ReservedRegion.ID](./id-swift.property.md)
  The identifier of the region.
- [ReservedRegion.ID](./id-swift.struct.md)
  An identifier for a reserved region.
- [ReservedRegion.Kind](./kind-swift.struct.md)
  A kind of reserved region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion/kind-swift.property)*