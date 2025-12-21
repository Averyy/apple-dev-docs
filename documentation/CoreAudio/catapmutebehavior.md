# CATapMuteBehavior

**Framework**: Core Audio  
**Kind**: enum

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
enum CATapMuteBehavior
```

#### Overview

CATapMuteBehavior describes the playback behavior of the process being tapped. The default value is CATapUnmuted.

```None
Audio is captured by the tap and also sent to the audio hardware
```

```None
Audio is captured by the tap but no audio is sent from the process to the audio hardware
```

```None
Audio is captured by the tap and also sent to the audio hardware until the tap is read by another audio client. 
For the duration of the read activity on the tap no audio is sent to the audio hardware.
```

## Topics

### Enumeration Cases
- [CATapMuteBehavior.muted](catapmutebehavior/muted.md)
- [CATapMuteBehavior.mutedWhenTapped](catapmutebehavior/mutedwhentapped.md)
- [CATapMuteBehavior.unmuted](catapmutebehavior/unmuted.md)
### Initializers
- [init?(rawValue: Int)](catapmutebehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Anonymous](1580748-anonymous.md)
- [Anonymous](1580731-anonymous.md)
- [Anonymous](1580722-anonymous.md)
- [Anonymous](1580720-anonymous.md)
- [Anonymous](1580736-anonymous.md)
- [Anonymous](1580737-anonymous.md)
- [Anonymous](1580746-anonymous.md)
- [Anonymous](1580723-anonymous.md)
- [Anonymous](1580747-anonymous.md)
- [Anonymous](1580749-anonymous.md)
- [Anonymous](1580719-anonymous.md)
- [Anonymous](1580715-anonymous.md)
- [Anonymous](1580740-anonymous.md)
- [Anonymous](1580741-anonymous.md)
- [Anonymous](1580726-anonymous.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapmutebehavior)*