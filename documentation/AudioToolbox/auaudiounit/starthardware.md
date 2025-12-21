# startHardware()

**Framework**: Audio Toolbox  
**Kind**: method

Starts the audio hardware.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func startHardware() throws
```

#### Discussion

- [`false`](https://developer.apple.com/documentation/Swift/false) if the operation failed.

#### Discussion

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

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
- [var isOutputEnabled: Bool](auaudiounit/isoutputenabled.md)
  A flag enabling audio output from the unit.
- [var inputHandler: AUInputHandler?](auaudiounit/inputhandler.md)
  The block that the output unit will call to notify when input is available.
- [var outputProvider: AURenderPullInputBlock?](auaudiounit/outputprovider.md)
  The block that the output unit will call to get audio to send to the output.
- [var deviceInputLatency: TimeInterval](auaudiounit/deviceinputlatency.md)
  The audio device’s input latency, in seconds.
- [var deviceOutputLatency: TimeInterval](auaudiounit/deviceoutputlatency.md)
  The audio devic’s output latency, in seconds.
- [func stopHardware()](auaudiounit/stophardware.md)
  Stops the audio hardware.
- [typealias AURenderPullInputBlock](aurenderpullinputblock.md)
  A block to supply audio input to a render block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/starthardware())*