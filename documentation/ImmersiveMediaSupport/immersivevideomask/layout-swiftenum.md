# ImmersiveVideoMask.Layout

**Framework**: Immersive Media Support  
**Kind**: enum

Represents the layout of the video mask

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Layout
```

## Topics

### Enumeration Cases
- [ImmersiveVideoMask.Layout.mono](immersivevideomask/layout-swift.enum/mono.md)
  Represents mono mask layout i.e single mask for both the eyes
- [ImmersiveVideoMask.Layout.overUnder](immersivevideomask/layout-swift.enum/overunder.md)
  Represents over under mask layout
- [ImmersiveVideoMask.Layout.separate](immersivevideomask/layout-swift.enum/separate.md)
  Represents stereo mask but separated
- [ImmersiveVideoMask.Layout.sideBySide](immersivevideomask/layout-swift.enum/sidebyside.md)
  Represents side by side mask layout
### Initializers
- [init?(rawValue: Int32)](immersivevideomask/layout-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int32](immersivevideomask/layout-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ImmersiveVideoMask.Layout.RawValue](immersivevideomask/layout-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](immersivevideomask/layout-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](immersivevideomask/layout-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask/layout-swift.enum)*