# ImmersiveVideoFrame.VideoLayout

**Framework**: Immersive Media Support  
**Kind**: enum

A value specifying the layout of left and right eyes within an immersive video frame.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum VideoLayout
```

## Topics

### Operators
- [static func == (ImmersiveVideoFrame.VideoLayout, ImmersiveVideoFrame.VideoLayout) -> Bool](immersivevideoframe/videolayout/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ImmersiveVideoFrame.VideoLayout.mono](immersivevideoframe/videolayout/mono.md)
  A value representing mono video layout i.e single frame for both the eyes
- [ImmersiveVideoFrame.VideoLayout.overUnder](immersivevideoframe/videolayout/overunder.md)
  A value representing over under video layout
- [ImmersiveVideoFrame.VideoLayout.separate](immersivevideoframe/videolayout/separate.md)
  A value representing stereo video but separated i.e MV-HEVC videos have such layout
- [ImmersiveVideoFrame.VideoLayout.sideBySide](immersivevideoframe/videolayout/sidebyside.md)
  A value representing side by side video layout
### Instance Properties
- [var hashValue: Int](immersivevideoframe/videolayout/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](immersivevideoframe/videolayout/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](immersivevideoframe/videolayout/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideoframe/videolayout)*