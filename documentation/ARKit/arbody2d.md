# ARBody2D

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

The screen-space representation of a person ARKit recognizes in the camera feed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
class ARBody2D
```

```objc
@interface ARBody2D : NSObject
```

## Overview

When ARKit recognizes a person in the camera feed, it estimates the screen-space location of the body’s joints and provides the location to you through current frame’s [`detectedBody`](./arframe/detectedbody.md).

## Topics

### Getting Joint Information
- [var skeleton: ARSkeleton2D](./arbody2d/skeleton.md)
  An object that contains the screen position of a body’s joints.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking for people
- [var detectedBody: ARBody2D?](./arframe/detectedbody.md)
  The screen position information of a body that ARKit recognizes in the camera image.
- [var segmentationBuffer: CVPixelBuffer?](./arframe/segmentationbuffer.md)
  A buffer that contains pixel information identifying the shape of objects from the camera feed that you use to occlude virtual content.
- [var estimatedDepthData: CVPixelBuffer?](./arframe/estimateddepthdata.md)
  A buffer that represents the estimated depth values from the camera feed that you use to occlude virtual content.
- [ARFrame.SegmentationClass](./arframe/segmentationclass.md)
  A categorization of a pixel that defines a type of content you use to occlude your app’s virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbody2d)*