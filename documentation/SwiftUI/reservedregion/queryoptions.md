# ReservedRegion.QueryOptions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Options for querying reserved regions.

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
@frozen
struct QueryOptions
```

## Overview

Pass query options to [`reservedRegions(kind:options:layoutDirectionBehavior:)`](../geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md) to change which regions you get.

## Topics

### Getting query options
- [static var includeInactive: ReservedRegion.QueryOptions](./queryoptions/includeinactive.md)
  An option that includes inactive reserved regions in the results.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Inspecting reserved regions
- [func reservedRegions(kind: ReservedRegion.Kind, options: ReservedRegion.QueryOptions, layoutDirectionBehavior: LayoutDirectionBehavior) -> [ReservedRegion]](../geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md)
  Returns an array of reserved regions that match the selection options you specify.
- [struct ReservedRegion](../reservedregion.md)
  A region within a view’s coordinate space that another entity reserves.
- [ReservedRegion.Kind](./kind-swift.struct.md)
  A kind of reserved region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion/queryoptions)*