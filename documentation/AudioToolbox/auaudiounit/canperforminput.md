# canPerformInput

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

Determines whether the I/O device can perform input.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var canPerformInput: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canPerformInput;
```

## See Also

### Configuring the Device
- [var deviceID: AUAudioObjectID](./deviceid.md)
  Gets the I/O hardware device.
- [func setDeviceID(AUAudioObjectID) throws](./setdeviceid%28_%29.md)
  Sets the I/O hardware device.
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
- [func startHardware() throws](./starthardware%28%29.md)
  Starts the audio hardware.
- [func stopHardware()](./stophardware%28%29.md)
  Stops the audio hardware.
- [typealias AURenderPullInputBlock](../aurenderpullinputblock.md)
  A block to supply audio input to a render block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/canperforminput)*