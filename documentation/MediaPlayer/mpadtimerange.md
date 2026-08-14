# MPAdTimeRange

**Framework**: Media Player  
**Kind**: class

An object that represents a time range where an ad break exists in the current player.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MPAdTimeRange
```

#### Overview

This value must be in bounds of the duration of the current player item.

## Topics

### Creating an Ad Time Range
- [init(CMTimeRange)](mpadtimerange/init(_:).md)
  Creates a Media Player time range that indicates where an ad break exists in the current player.
### Inspecting an Ad Time Range
- [var timeRange: CMTimeRange](mpadtimerange/timerange.md)
  A Media Player time range that indicates where an ad break exists in the current player.
### Initializers
- [init(timeRange: CMTimeRange)](mpadtimerange/init(timerange:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpadtimerange)*