# MTLCreateSystemDefaultDevice()

**Framework**: Metal  
**Kind**: func

Returns the device instance Metal selects as the default.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func MTLCreateSystemDefaultDevice() -> (any MTLDevice)?
```

## Mentions

- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
- [Getting the Default GPU](getting-the-default-gpu.md)

#### Return Value

A device object.

#### Discussion

In macOS, in order for the system to provide a default Metal device object, you must link to the [`Core Graphics`](https://developer.apple.com/documentation/CoreGraphics) framework. You usually need to do this explicitly if you’re writing apps that don’t use graphics by default, such as command line tools.

## See Also

- [Getting the Default GPU](getting-the-default-gpu.md)
  Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU Features and Metal Software Versions](detecting-gpu-features-and-metal-software-versions.md)
  Use the device object’s properties to determine how you perform tasks in Metal.
- [protocol MTLDevice](mtldevice.md)
  The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.
- [Multi-GPU Systems](multi-gpu-systems.md)
  Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcreatesystemdefaultdevice())*