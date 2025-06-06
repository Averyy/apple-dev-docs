# init(inputPorts:output:)

**Framework**: AVFoundation  
**Kind**: init

Creates a capture connection that represents a connection between multiple input ports and an output.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
init(inputPorts ports: [AVCaptureInput.Port], output: AVCaptureOutput)
```

#### Return Value

A capture connection that represents a connection between `ports` and `output`.

#### Discussion

You can add the connection this method returns to an [`AVCaptureSession`](avcapturesession.md) instance with the [`addConnection(_:)`](avcapturesession/addconnection(_:).md) method.

The [`addInput(_:)`](avcapturesession/addinput(_:).md): or [`addOutput(_:)`](avcapturesession/addoutput(_:).md) methods automatically form connections between all compatible inputs and outputs. You don’t need to manually create and add connections to the session unless you use the primitive [`addInputWithNoConnections(_:)`](avcapturesession/addinputwithnoconnections(_:).md) and [`addOutputWithNoConnections(_:)`](avcapturesession/addoutputwithnoconnections(_:).md) methods.

## Parameters

- `ports`: An array of   instances that relate to   instances.
- `output`: An   instance.

## See Also

- [init(inputPort: AVCaptureInput.Port, videoPreviewLayer: AVCaptureVideoPreviewLayer)](avcaptureconnection/init(inputport:videopreviewlayer:).md)
  Creates a capture connection that represents a connection between an input port and a video preview layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/init(inputports:output:))*