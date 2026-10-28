# CATapMuteBehavior

**Framework**: Core Audio  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
enum CATapMuteBehavior
```

```c
enum CATapMuteBehavior : NSInteger;
```

## Overview

CATapMuteBehavior describes the playback behavior of the process being tapped. The default value is CATapUnmuted.

```
Audio is captured by the tap and also sent to the audio hardware
```

```
Audio is captured by the tap but no audio is sent from the process to the audio hardware
```

```
Audio is captured by the tap and also sent to the audio hardware until the tap is read by another audio client. 
For the duration of the read activity on the tap no audio is sent to the audio hardware.
```

## Topics

### Enumeration Cases
- [CATapMuteBehavior.muted](./catapmutebehavior/muted.md)
- [CATapMuteBehavior.mutedWhenTapped](./catapmutebehavior/mutedwhentapped.md)
- [CATapMuteBehavior.unmuted](./catapmutebehavior/unmuted.md)
### Initializers
- [init?(rawValue: Int)](./catapmutebehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [Anonymous](./api-1580748-anonymous.md)
- [Anonymous](./api-1580731-anonymous.md)
- [Anonymous](./api-1580722-anonymous.md)
- [Anonymous](./api-1580720-anonymous.md)
- [Anonymous](./api-1580736-anonymous.md)
- [Anonymous](./api-1580737-anonymous.md)
- [Anonymous](./api-1580746-anonymous.md)
- [Anonymous](./api-1580723-anonymous.md)
- [Anonymous](./api-1580747-anonymous.md)
- [Anonymous](./api-1580749-anonymous.md)
- [Anonymous](./api-1580719-anonymous.md)
- [Anonymous](./api-1580715-anonymous.md)
- [Anonymous](./api-1580740-anonymous.md)
- [Anonymous](./api-1580741-anonymous.md)
- [Anonymous](./api-1580726-anonymous.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapmutebehavior)*