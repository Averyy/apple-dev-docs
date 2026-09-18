# ReservedRegion.Kind

**Framework**: SwiftUI  
**Kind**: struct

A kind of reserved region.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
struct Kind
```

## Topics

### Getting reserved region kinds
- [static var division: ReservedRegion.Kind](reservedregion/kind-swift.struct/division.md)
  A region where content should split into two separate regions.
- [static var occlusion: ReservedRegion.Kind](reservedregion/kind-swift.struct/occlusion.md)
  A region that is occluded by an element.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func reservedRegions(kind: ReservedRegion.Kind, options: ReservedRegion.QueryOptions, layoutDirectionBehavior: LayoutDirectionBehavior) -> [ReservedRegion]](geometryproxy/reservedregions(kind:options:layoutdirectionbehavior:).md)
  Returns an array of reserved regions that match the selection options you specify.
- [struct ReservedRegion](reservedregion.md)
  A region within a view’s coordinate space that another entity reserves.
- [ReservedRegion.QueryOptions](reservedregion/queryoptions.md)
  Options for querying reserved regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion/kind-swift.struct)*