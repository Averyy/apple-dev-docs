# ReservedRegion.QueryOptions

**Framework**: SwiftUI  
**Kind**: struct

Options for querying reserved regions.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@frozen
struct QueryOptions
```

## Topics

### Getting query options
- [static var includeInactive: ReservedRegion.QueryOptions](reservedregion/queryoptions/includeinactive.md)
  Include inactive reserved regions.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func reservedRegions(kind: ReservedRegion.Kind, options: ReservedRegion.QueryOptions, layoutDirectionBehavior: LayoutDirectionBehavior) -> [ReservedRegion]](geometryproxy/reservedregions(kind:options:layoutdirectionbehavior:).md)
  Returns an array of reserved regions that match the selection options you specify.
- [struct ReservedRegion](reservedregion.md)
  A region within a view’s coordinate space that another entity reserves.
- [ReservedRegion.Kind](reservedregion/kind-swift.struct.md)
  A kind of reserved region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion/queryoptions)*