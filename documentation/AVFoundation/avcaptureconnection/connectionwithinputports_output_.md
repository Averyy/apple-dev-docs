# connectionWithInputPorts:output:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a capture connection that represents a connection between multiple input ports and an output.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```objc
+ (instancetype) connectionWithInputPorts:(NSArray<AVCaptureInputPort *> *) ports output:(AVCaptureOutput *) output;
```

## Return Value

A capture connection that represents a connection between `ports` and `output`.

## Discussion

You can add the connection this method returns to an [`AVCaptureSession`](../avcapturesession.md) instance with the [`addConnection(_:)`](../avcapturesession/addconnection%28_%29.md) method.

The [`addInput(_:)`](../avcapturesession/addinput%28_%29.md): or [`addOutput(_:)`](../avcapturesession/addoutput%28_%29.md) methods automatically form connections between all compatible inputs and outputs. You don’t need to manually create and add connections to the session unless you use the primitive [`addInputWithNoConnections(_:)`](../avcapturesession/addinputwithnoconnections%28_%29.md) and [`addOutputWithNoConnections(_:)`](../avcapturesession/addoutputwithnoconnections%28_%29.md) methods.

## Parameters

- `ports`: An array of [`AVCaptureInput.Port`](../avcaptureinput/port.md) instances that relate to [`AVCaptureInput`](../avcaptureinput.md) instances.
- `output`: An [`AVCaptureOutput`](../avcaptureoutput.md) instance.

## See Also

### Creating a connection
- [init(inputPorts: [AVCaptureInput.Port], output: AVCaptureOutput)](./init%28inputports,output%29.md)
  Creates a capture connection that represents a connection between multiple input ports and an output.
- [init(inputPort: AVCaptureInput.Port, videoPreviewLayer: AVCaptureVideoPreviewLayer)](./init%28inputport,videopreviewlayer%29.md)
  Creates a capture connection that represents a connection between an input port and a video preview layer.
- [+ connectionWithInputPort:videoPreviewLayer:](./connectionwithinputport_videopreviewlayer_.md)
  Returns a capture connection that represents a connection between an input port and a video preview layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/connectionwithinputports:output:)*