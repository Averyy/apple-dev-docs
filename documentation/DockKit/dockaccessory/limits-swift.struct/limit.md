# DockAccessory.Limits.Limit

**Framework**: DockKit  
**Kind**: struct  
**Role**: Structure

A description of a limit placed on an axis of rotation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Limit
```

## Overview

Zero is the default minimum angular speed. Invalid limit specifications include minimum position greater than maximum position, minimum position equals maximum position, and maximum speed is less than zero.

## Topics

### Limiting speed and position
- [let maximumSpeed: Double](./limit/maximumspeed.md)
  The maximum speed that the dock accessory moves.
- [let positionRange: Range<Double>](./limit/positionrange.md)
  The valid range that the dock accessory moves.
### Initializers
- [init(positionRange: Range<Double>, maximumSpeed: Double) throws](./limit/init%28positionrange,maximumspeed%29.md)

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/limits-swift.struct/limit)*