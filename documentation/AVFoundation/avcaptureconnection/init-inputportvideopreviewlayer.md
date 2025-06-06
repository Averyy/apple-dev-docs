# init(inputPort:videoPreviewLayer:)

**Framework**: AVFoundation  
**Kind**: init

Creates a capture connection that represents a connection between an input port and a video preview layer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
init(inputPort port: AVCaptureInput.Port, videoPreviewLayer layer: AVCaptureVideoPreviewLayer)
```

#### Return Value

A capture connection that represents a connection between `port` and `layer`.

#### Discussion

You can add the connection this method returns to an [`AVCaptureSession`](avcapturesession.md) instance with the [`addConnection(_:)`](avcapturesession/addconnection(_:).md) method.

The [`addInput(_:)`](avcapturesession/addinput(_:).md): or [`addOutput(_:)`](avcapturesession/addoutput(_:).md) methods automatically form connections between all compatible inputs and outputs. You don’t need to manually create and add connections to the session unless you use the primitive [`addInputWithNoConnections(_:)`](avcapturesession/addinputwithnoconnections(_:).md) and [`addOutputWithNoConnections(_:)`](avcapturesession/addoutputwithnoconnections(_:).md) methods.

## Parameters

- `port`: An   instance that relates to an   instance.
- `layer`: An   instance.

## See Also

- [init(inputPorts: [AVCaptureInput.Port], output: AVCaptureOutput)](avcaptureconnection/init(inputports:output:).md)
  Creates a capture connection that represents a connection between multiple input ports and an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/init(inputport:videopreviewlayer:))*