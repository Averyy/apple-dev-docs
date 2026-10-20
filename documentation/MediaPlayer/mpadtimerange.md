# MPAdTimeRange

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPAdTimeRange : NSObject
```

#### Overview

This value must be in bounds of the duration of the current player item.

## Topics

### Creating an Ad Time Range
- [init(CMTimeRange)](./mpadtimerange/init%28_%29.md)
  Creates a Media Player time range that indicates where an ad break exists in the current player.
### Inspecting an Ad Time Range
- [var timeRange: CMTimeRange](./mpadtimerange/timerange.md)
  A Media Player time range that indicates where an ad break exists in the current player.
### Initializers
- [init(timeRange: CMTimeRange)](./mpadtimerange/init%28timerange%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpadtimerange)*