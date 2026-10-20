# RPBroadcastSampleHandler

**Framework**: ReplayKit  
**Kind**: class  
**Role**: Class

An object that processes buffer objects as received from ReplayKit.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
class RPBroadcastSampleHandler
```

```objc
@interface RPBroadcastSampleHandler : RPBroadcastHandler
```

#### Overview

To handle [`CMSampleBuffer`](../CoreMedia/cmsamplebuffer.md) objects as captured by ReplayKit, you subclass `RPBroadcastSampleHandler`. You enable this mode of handling by setting `RPBroadcastProcessMode` in the extension’s `Info.plist` file to `RPBroadcastProcessModeSampleBuffer`.

In your subclass, implement the [`processSampleBuffer(_:with:)`](./rpbroadcastsamplehandler/processsamplebuffer%28_,with%29.md) method to handle video and audio buffers, as well as the [`broadcastStarted(withSetupInfo:)`](./rpbroadcastsamplehandler/broadcaststarted%28withsetupinfo%29.md), [`broadcastFinished()`](./rpbroadcastsamplehandler/broadcastfinished%28%29.md), [`broadcastPaused()`](./rpbroadcastsamplehandler/broadcastpaused%28%29.md), and [`broadcastResumed()`](./rpbroadcastsamplehandler/broadcastresumed%28%29.md) methods to handle starting and stopping the broadcast.

ReplayKit invokes methods in your `RPBroadcastSampleHandler` subclass in a serial fashion. After invoking one method, ReplayKit won’t invoke another method until the first method returns. That means it’s safe for your implementations to update their stored state without the use of locks or synchronization to provide thread safety.

## Topics

### Handling Sample Buffer Clips
- [func broadcastStarted(withSetupInfo: [String : NSObject]?)](./rpbroadcastsamplehandler/broadcaststarted%28withsetupinfo%29.md)
  Perform any required actions after starting a live broadcast.
- [func broadcastPaused()](./rpbroadcastsamplehandler/broadcastpaused%28%29.md)
  Perform any required actions after a live broadcast is paused.
- [func broadcastResumed()](./rpbroadcastsamplehandler/broadcastresumed%28%29.md)
  Perform any required actions after a live broadcast is resumed.
- [func broadcastFinished()](./rpbroadcastsamplehandler/broadcastfinished%28%29.md)
  Perform any required actions after a live broadcast is finished.
- [func broadcastAnnotated(withApplicationInfo: [AnyHashable : Any])](./rpbroadcastsamplehandler/broadcastannotated%28withapplicationinfo%29.md)
  Perform any required actions after starting a live broadcast.
- [let RPApplicationInfoBundleIdentifierKey: String](./rpapplicationinfobundleidentifierkey.md)
  The key to retrieve the app’s bundle identifier from the user-information dictionary.
- [func processSampleBuffer(CMSampleBuffer, with: RPSampleBufferType)](./rpbroadcastsamplehandler/processsamplebuffer%28_,with%29.md)
  Processes video and audio data as it becomes available during a live broadcast.
- [let RPVideoSampleOrientationKey: String](./rpvideosampleorientationkey.md)
  The sample attachment key that describes the video orientation.
- [func finishBroadcastWithError(any Error)](./rpbroadcastsamplehandler/finishbroadcastwitherror%28_%29.md)
  Stops the broadcast and passes an error back to the broadcasting app.

## Relationships

### Inherits From
- [RPBroadcastHandler](./rpbroadcasthandler.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Media Clip Processing
- [class RPBroadcastController](./rpbroadcastcontroller.md)
  An object containing methods for starting and controlling a broadcast.
- [class RPBroadcastHandler](./rpbroadcasthandler.md)
  An object that sends messages to the broadcasting app.
- [class RPBroadcastMP4ClipHandler](./rpbroadcastmp4cliphandler.md)
  An object that processes MP4 movie clips from ReplayKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler)*