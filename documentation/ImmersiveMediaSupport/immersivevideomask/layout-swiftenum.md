# ImmersiveVideoMask.Layout

**Framework**: Immersive Media Support  
**Kind**: enum

A value representing the layout of the video mask.

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
  A value representing mono mask layout i.e single mask for both the eyes
- [ImmersiveVideoMask.Layout.overUnder](immersivevideomask/layout-swift.enum/overunder.md)
  A value representing over under mask layout
- [ImmersiveVideoMask.Layout.separate](immersivevideomask/layout-swift.enum/separate.md)
  A value representing stereo mask but separated
- [ImmersiveVideoMask.Layout.sideBySide](immersivevideomask/layout-swift.enum/sidebyside.md)
  A value representing side by side mask layout
### Operators
- [static func == (ImmersiveVideoMask.Layout, ImmersiveVideoMask.Layout) -> Bool](immersivevideomask/layout-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](immersivevideomask/layout-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](immersivevideomask/layout-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](immersivevideomask/layout-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask/layout-swift.enum)*