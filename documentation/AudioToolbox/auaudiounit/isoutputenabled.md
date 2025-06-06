# isOutputEnabled

**Framework**: Audio Toolbox  
**Kind**: property

A flag enabling audio output from the unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var isOutputEnabled: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var deviceID: AUAudioObjectID](auaudiounit/deviceid.md)
  Gets the I/O hardware device.
- [func setDeviceID(AUAudioObjectID) throws](auaudiounit/setdeviceid(_:).md)
  Sets the I/O hardware device.
- [var canPerformInput: Bool](auaudiounit/canperforminput.md)
  Determines whether the I/O device can perform input.
- [var canPerformOutput: Bool](auaudiounit/canperformoutput.md)
  Determines whether the I/O device can perform output.
- [var isInputEnabled: Bool](auaudiounit/isinputenabled.md)
  A flag enabling audio input from the unit.
- [var inputHandler: AUInputHandler?](auaudiounit/inputhandler.md)
  The block that the output unit will call to notify when input is available.
- [var outputProvider: AURenderPullInputBlock?](auaudiounit/outputprovider.md)
  The block that the output unit will call to get audio to send to the output.
- [var deviceInputLatency: TimeInterval](auaudiounit/deviceinputlatency.md)
  The audio device’s input latency, in seconds.
- [var deviceOutputLatency: TimeInterval](auaudiounit/deviceoutputlatency.md)
  The audio devic’s output latency, in seconds.
- [func startHardware() throws](auaudiounit/starthardware.md)
  Starts the audio hardware.
- [func stopHardware()](auaudiounit/stophardware.md)
  Stops the audio hardware.
- [typealias AURenderPullInputBlock](aurenderpullinputblock.md)
  A block to supply audio input to a render block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/isoutputenabled)*