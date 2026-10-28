# startHardware()

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Starts the audio hardware.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func startHardware() throws
```

```objc
- (BOOL) startHardwareAndReturnError:(NSError **) outError;
```

## Discussion

- [`false`](../../Swift/false.md) if the operation failed.

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Configuring the Device
- [var deviceID: AUAudioObjectID](./deviceid.md)
  Gets the I/O hardware device.
- [func setDeviceID(AUAudioObjectID) throws](./setdeviceid%28_%29.md)
  Sets the I/O hardware device.
- [var canPerformInput: Bool](./canperforminput.md)
  Determines whether the I/O device can perform input.
- [var canPerformOutput: Bool](./canperformoutput.md)
  Determines whether the I/O device can perform output.
- [var isInputEnabled: Bool](./isinputenabled.md)
  A flag enabling audio input from the unit.
- [var isOutputEnabled: Bool](./isoutputenabled.md)
  A flag enabling audio output from the unit.
- [var inputHandler: AUInputHandler?](./inputhandler.md)
  The block that the output unit will call to notify when input is available.
- [var outputProvider: AURenderPullInputBlock?](./outputprovider.md)
  The block that the output unit will call to get audio to send to the output.
- [var deviceInputLatency: TimeInterval](./deviceinputlatency.md)
  The audio device’s input latency, in seconds.
- [var deviceOutputLatency: TimeInterval](./deviceoutputlatency.md)
  The audio devic’s output latency, in seconds.
- [func stopHardware()](./stophardware%28%29.md)
  Stops the audio hardware.
- [typealias AURenderPullInputBlock](../aurenderpullinputblock.md)
  A block to supply audio input to a render block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/starthardware())*