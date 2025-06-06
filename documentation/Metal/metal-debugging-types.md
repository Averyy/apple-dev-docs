# Metal Debugging Types

**Framework**: Metal

Create capture managers and capture scopes, and review a GPU device’s log after it runs a command buffer.

## Topics

### Frame Capture
- [class MTLCaptureDescriptor](mtlcapturedescriptor.md)
  A configuration for a Metal capture session.
- [class MTLCaptureManager](mtlcapturemanager.md)
  An instance you use to capture Metal command data in your app.
- [enum MTLCaptureDestination](mtlcapturedestination.md)
  The kinds of destinations for captured command data.
- [protocol MTLCaptureScope](mtlcapturescope.md)
  A protocol that defines custom boundaries for a GPU frame capture.
### Capture Errors
- [enum MTLCaptureError](mtlcaptureerror.md)
  Errors returned by capture sessions.
- [let MTLCaptureErrorDomain: String](mtlcaptureerrordomain.md)
  The error domain for capture errors.
### Shader Logs
- [protocol MTLFunctionLog](mtlfunctionlog.md)
  A log entry a Metal device generates when the it runs a command buffer.
- [struct MTLLogContainer](mtllogcontainer-swift.struct.md)
  A collection of logged messages, created when a Metal device runs a command buffer.

## See Also

- [Metal developer workflows](../Xcode/Metal-developer-workflows.md)
  Locate and fix issues related to your app’s use of the Metal API and GPU functions.
- [Metal debugger](../Xcode/Metal-debugger.md)
  Debug and profile your Metal workload with a GPU trace.
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md)
  Fix performance glitches and develop default settings for smooth experiences on Apple platforms using the powerful suite of Metal development tools.
- [Capturing Metal Commands Programmatically](capturing-metal-commands-programmatically.md)
  Invoke Metal’s frame capture from your app, then save the resulting GPU trace to a file or view it in Xcode.
- [Supporting Simulator in a Metal app](supporting-simulator-in-a-metal-app.md)
  Configure alternative render paths in your Metal app to enable running your app in Simulator.
- [Analyzing the memory usage of your Metal app](../Xcode/Analyzing-the-memory-usage-of-your-Metal-app.md)
  Keep your app alive in the background by managing its memory footprint.
- [Analyzing the performance of your Metal app](../Xcode/Analyzing-the-performance-of-your-Metal-app.md)
  Ensure consistent, smooth rendering by profiling your app’s frame time.
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
  Prototype and test your Metal apps in Simulator.
- [GPU Counters and Counter Sample Buffers](gpu-counters-and-counter-sample-buffers.md)
  Retrieve runtime data from a GPU device by sampling one or more of its counters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/metal-debugging-types)*