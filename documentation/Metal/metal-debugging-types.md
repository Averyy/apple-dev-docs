# Metal debugging types

**Framework**: Metal

Create capture managers and capture scopes, and review a GPU device’s log after it runs a command buffer.

## Topics

### Frame capture
- [class MTLCaptureDescriptor](mtlcapturedescriptor.md)
  A configuration for a Metal capture session.
- [class MTLCaptureManager](mtlcapturemanager.md)
  An instance you use to capture Metal command data in your app.
- [enum MTLCaptureDestination](mtlcapturedestination.md)
  The kinds of destinations for captured command data.
- [protocol MTLCaptureScope](mtlcapturescope.md)
  A type that can programmatically customize a GPU frame capture.
### Capture errors
- [enum MTLCaptureError](mtlcaptureerror.md)
  Errors returned by capture sessions.
- [let MTLCaptureErrorDomain: String](mtlcaptureerrordomain.md)
  The error domain for capture errors.
### Shader logs
- [protocol MTLFunctionLog](mtlfunctionlog.md)
  A log entry a Metal device generates when the it runs a command buffer.
- [struct MTLLogContainer](mtllogcontainer-swift.struct.md)
  A collection of logged messages, created when a Metal device runs a command buffer.

## See Also

- [Supporting Simulator in a Metal app](supporting-simulator-in-a-metal-app.md)
  Configure alternative render paths in your Metal app to enable running your app in Simulator.
- [Capturing Metal commands programmatically](capturing-metal-commands-programmatically.md)
  Invoke a Metal frame capture from your app, then save the resulting GPU trace to a file or view it in Xcode.
- [Logging shader debug messages](logging-shader-debug-messages.md)
  Print debugging messages that a shader generates using shader logging.
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
  Prototype and test your Metal apps in Simulator.
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md)
  Fix performance glitches and develop default settings for smooth experiences on Apple platforms using the powerful suite of Metal development tools.
- [Metal debugger](../Xcode/Metal-debugger.md)
  Debug and profile your Metal workload with a GPU trace.
- [Metal developer workflows](../Xcode/Metal-developer-workflows.md)
  Locate and fix issues related to your app’s use of the Metal API and GPU functions.
- [GPU counters and counter sample buffers](gpu-counters-and-counter-sample-buffers.md)
  Retrieve runtime data from a GPU device by sampling one or more of its counters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/metal-debugging-types)*