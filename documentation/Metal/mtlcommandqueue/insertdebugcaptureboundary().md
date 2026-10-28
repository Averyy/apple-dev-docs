# insertDebugCaptureBoundary()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs Xcode about when GPU Frame Capture starts and stops.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.13
- tvOS - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`MTLCaptureManager`](../mtlcapturemanager.md) and [`MTLCaptureScope`](../mtlcapturescope.md) instead. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md) for more information.

## Declaration

```swift
func insertDebugCaptureBoundary()
```

```objc
- (void) insertDebugCaptureBoundary;
```

## Discussion

You can explicitly define the boundary between two GPU captures by calling this method, which overrides the default behavior in Xcode when you caputre a GPU frame. If your app doesn’t call the method, Xcode adds a frame boundary each time your app calls the [`present(_:)`](../mtlcommandbuffer/present%28_%29.md) or [`present(_:atTime:)`](../mtlcommandbuffer/present%28_,attime%29.md) methods.

For example, an app with a single drawable may not need this method because the default behavior’s implicit frame boundaries are appropriate for that scenario.

![A timeline diagram that shows a single drawable that presents a sequence of four frames at regular intervals, each of which implicitly creates a frame capture.](https://developer.apple.com/tutorials/images/com.apple.metal/insertDebugCaptureBoundary-1@2x.png)

However, you may want to create explicit frame boundaries for apps with multiple drawables that produce frames at different rates.

![A timeline diagram that shows three drawables, each of which presents their own sequence of frames at regular, but differing, intervals from each other. Drawable A presents four frames in the time span, Drawable B presents two frames, and Drawable C presents three frames, the first of which starts at the same time as  Drawable A’s second frame.](https://developer.apple.com/tutorials/images/com.apple.metal/insertDebugCaptureBoundary-2@2x.png)

In this example scenario, the app uses three drawables, each of which presents their frames at different rates or times. The developer can use this method to add arbitrary boundaries that create two captures. The first capture contains the first two frames from Drawable A, the first frame from Drawable B, and the first frame from Drawable C. The second capture contains the third and fourth frames from Drawable A, the second frame from Drawable B, and the second and third frames from Drawable C.

> ⚠️ **Warning**:  Don’t call this method from within the completion handler you pass to [`addCompletedHandler(_:)`](../mtlcommandbuffer/addcompletedhandler%28_%29.md) because it can trigger a deadlock when you capture a GPU frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/insertdebugcaptureboundary())*