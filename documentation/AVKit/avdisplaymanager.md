# AVDisplayManager

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A tvOS management object that controls whether a TV switches modes to match the video’s native mode.

**Availability**:
- tvOS 11.2+
- visionOS 1.0+

## Declaration

```swift
class AVDisplayManager
```

```objc
@interface AVDisplayManager : NSObject
```

#### Overview

If you set the display manager’s [`preferredDisplayCriteria`](./avdisplaymanager/preferreddisplaycriteria.md), when a user enables a Match Content setting, the TV attempts to change modes to match the currently playing video’s native display criteria.

> ❗ **Important**:  Don’t directly instantiate a display manager object. Instead, access the current instance from the key window’s [`avDisplayManager`](../UIKit/uiwindow/avdisplaymanager.md) property.

## Topics

### Matching a video’s native display mode
- [var preferredDisplayCriteria: AVDisplayCriteria?](./avdisplaymanager/preferreddisplaycriteria.md)
  A hint for the TV to set the display mode to best match the currently playing content’s display criteria.
- [var isDisplayCriteriaMatchingEnabled: Bool](./avdisplaymanager/isdisplaycriteriamatchingenabled.md)
  A Boolean value that indicates whether the user has enabled display critera matching.
- [var isDisplayModeSwitchInProgress: Bool](./avdisplaymanager/isdisplaymodeswitchinprogress.md)
  A Boolean value that indicates whether a display mode switch is in progress.

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

## See Also

### Display management
- [enum AVDisplayDynamicRange](./avdisplaydynamicrange.md)
  Describes how High Dynamic Range (HDR) video content renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avdisplaymanager)*