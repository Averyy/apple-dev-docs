# MTLCaptureManager

**Framework**: Metal  
**Kind**: class

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

#### Overview

Capture manager works with Metal’s frame capture feature to:

- Capture data about Metal commands programmatically. See [`Capturing a Metal workload programmatically`](https://developer.apple.com/documentation/Xcode/Capturing-a-Metal-workload-programmatically).
- Filter captured commands to a specific [`MTLDevice`](mtldevice.md), command queue, or capture scope.
- Assign a capture scope to use as the default when you click the camera button to invoke a frame capture from Xcode’s debug bar. See [`MTLCaptureScope`](mtlcapturescope.md).

The Metal debugger requires you to enable GPU Frame Capture in your project settings; see [`Capturing a Metal workload in Xcode`](https://developer.apple.com/documentation/Xcode/Capturing-a-Metal-workload-in-Xcode).

> ❗ **Important**:  The capture manager records commands within [`MTLCommandBuffer`](mtlcommandbuffer.md) objects that you create and commit while the capture session is active.

For more information about Metal frame capture, see [`Metal debugger`](https://developer.apple.com/documentation/Xcode/Metal-debugger).

## Topics

### Obtaining the Shared Capture Manager
- [class func shared() -> MTLCaptureManager](mtlcapturemanager/shared.md)
  Provides the shared capture manager for your Metal app.
### Querying Support for a Capture Destination
- [func supportsDestination(MTLCaptureDestination) -> Bool](mtlcapturemanager/supportsdestination(_:).md)
  Checks to see whether a particular capture destination is supported.
### Creating a Capture Scope
- [func makeCaptureScope(device: any MTLDevice) -> any MTLCaptureScope](mtlcapturemanager/makecapturescope(device:).md)
  Creates a capture scope for commands submitted to a specific device object.
- [func makeCaptureScope(commandQueue: any MTLCommandQueue) -> any MTLCaptureScope](mtlcapturemanager/makecapturescope(commandqueue:)-1rozd.md)
  Creates a capture scope for commands submitted to a specific command queue.
- [var defaultCaptureScope: (any MTLCaptureScope)?](mtlcapturemanager/defaultcapturescope.md)
  The capture scope to use when a capture is initiated in Xcode.
### Starting Capture
- [func startCapture(with: MTLCaptureDescriptor) throws](mtlcapturemanager/startcapture(with:).md)
  Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [func startCapture(device: any MTLDevice)](mtlcapturemanager/startcapture(device:).md)
  Starts capturing any of your app’s Metal commands that are executed by the device object.
- [func startCapture(commandQueue: any MTLCommandQueue)](mtlcapturemanager/startcapture(commandqueue:).md)
  Starts capturing any of your app’s Metal commands that are executed by the command queue.
- [func startCapture(scope: any MTLCaptureScope)](mtlcapturemanager/startcapture(scope:).md)
  Starts capturing any of your app’s Metal commands that are in the specified capture scope.
### Stopping Capture
- [func stopCapture()](mtlcapturemanager/stopcapture.md)
  Stops capturing Metal commands.
### Monitoring Capture
- [var isCapturing: Bool](mtlcapturemanager/iscapturing.md)
  A Boolean value that indicates whether Metal commands are being captured.
### Instance Methods
- [func makeCaptureScope(commandQueue: any MTL4CommandQueue) -> any MTLCaptureScope](mtlcapturemanager/makecapturescope(commandqueue:)-9wie3.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLCaptureDescriptor](mtlcapturedescriptor.md)
  A configuration for a Metal capture session.
- [enum MTLCaptureDestination](mtlcapturedestination.md)
  The kinds of destinations for captured command data.
- [protocol MTLCaptureScope](mtlcapturescope.md)
  A protocol that defines custom boundaries for a GPU frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager)*