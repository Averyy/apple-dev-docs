# MTLCaptureManager

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An instance you use to capture Metal command data in your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MTLCaptureManager
```

```objc
@interface MTLCaptureManager : NSObject
```

## Overview

A capture manager works with the frame capture feature to:

- Capture data about Metal commands programmatically. See [Capturing a Metal workload programmatically](../Xcode/capturing-a-metal-workload-programmatically.md).
- Only capture commands that apply to a specific [`MTLDevice`](./mtldevice.md), command queue, or [`MTLCaptureScope`](./mtlcapturescope.md) instance.
- Assign a default [`MTLCaptureScope`](./mtlcapturescope.md) instance for captures you create in Xcode by clicking the Capture GPU workload button in the debug bar, which has an icon with the Metal logo.

The Metal debugger requires you to enable GPU Frame Capture in your project settings; see [Capturing a Metal workload in Xcode](../Xcode/capturing-a-metal-workload-in-xcode.md).

> ❗ **Important**:  The capture manager records commands within the [`MTLCommandBuffer`](./mtlcommandbuffer.md) instance that you create and commit while the capture session is active.

For more information about Metal frame capture, see [Metal debugger](../Xcode/metal-debugger.md).

## Topics

### Obtaining the shared capture manager
- [class func shared() -> MTLCaptureManager](./mtlcapturemanager/shared%28%29.md)
  Provides the shared capture manager for your Metal app.
### Querying support for a capture destination
- [func supportsDestination(MTLCaptureDestination) -> Bool](./mtlcapturemanager/supportsdestination%28_%29.md)
  Checks to see whether a particular capture destination is supported.
### Creating a capture scope
- [func makeCaptureScope(device: any MTLDevice) -> any MTLCaptureScope](./mtlcapturemanager/makecapturescope%28device%29.md)
  Creates a capture scope for commands submitted to a specific device object.
- [func makeCaptureScope(commandQueue: any MTLCommandQueue) -> any MTLCaptureScope](./mtlcapturemanager/makecapturescope%28commandqueue%29-1rozd.md)
  Creates a capture scope for commands submitted to a specific command queue.
- [var defaultCaptureScope: (any MTLCaptureScope)?](./mtlcapturemanager/defaultcapturescope.md)
  The capture scope to use when a capture is initiated in Xcode.
### Starting capture
- [func startCapture(with: MTLCaptureDescriptor) throws](./mtlcapturemanager/startcapture%28with%29.md)
  Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [func startCapture(device: any MTLDevice)](./mtlcapturemanager/startcapture%28device%29.md)
  Starts capturing any of your app’s Metal commands that are executed by the device object.
- [func startCapture(commandQueue: any MTLCommandQueue)](./mtlcapturemanager/startcapture%28commandqueue%29.md)
  Starts capturing any of your app’s Metal commands that are executed by the command queue.
- [func startCapture(scope: any MTLCaptureScope)](./mtlcapturemanager/startcapture%28scope%29.md)
  Starts capturing any of your app’s Metal commands that are in the specified capture scope.
### Stopping capture
- [func stopCapture()](./mtlcapturemanager/stopcapture%28%29.md)
  Stops capturing Metal commands.
### Monitoring capture
- [var isCapturing: Bool](./mtlcapturemanager/iscapturing.md)
  A Boolean value that indicates whether Metal commands are being captured.
### Instance Methods
- [func makeCaptureScope(commandQueue: any MTL4CommandQueue) -> any MTLCaptureScope](./mtlcapturemanager/makecapturescope%28commandqueue%29-9wie3.md)
- [- init](./mtlcapturemanager/init.md)

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

### Frame capture
- [class MTLCaptureDescriptor](./mtlcapturedescriptor.md)
  A configuration for a Metal capture session.
- [enum MTLCaptureDestination](./mtlcapturedestination.md)
  The kinds of destinations for captured command data.
- [protocol MTLCaptureScope](./mtlcapturescope.md)
  A type that can programmatically customize a GPU frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager)*