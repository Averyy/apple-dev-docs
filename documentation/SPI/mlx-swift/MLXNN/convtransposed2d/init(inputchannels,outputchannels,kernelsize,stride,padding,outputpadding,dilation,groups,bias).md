---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/convtransposed2d/init(inputchannels:outputchannels:kernelsize:stride:padding:outputpadding:dilation:groups:bias:)"
framework: "mlx-swift/MLXNN"
---

# init(inputChannels:outputChannels:kernelSize:stride:padding:outputPadding:dilation:groups:bias:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies a 2-dimensional transposed convolution over the multi-channel input image.

## Declaration

```swift
init(inputChannels: Int, outputChannels: Int, kernelSize: IntOrPair, stride: IntOrPair = 1, padding: IntOrPair = 0, outputPadding: IntOrPair = 0, dilation: IntOrPair = 1, groups: Int = 1, bias: Bool = true)
```

#### Discussion

The channels are expected to be last i.e. the input shape should be `NHWC` where:

- `N` is the batch dimension
- `H` is the input image height
- `W` is the input image width
- `C` is the number of input channels

## Parameters

- `inputChannels`: Number of input channels (`C` from the discussion)
- `outputChannels`: Number of output channels
- `kernelSize`: Size of the convolution filters
- `stride`: Stride when applying the filter
- `padding`: How many positions to 0-pad the input with
- `outputPadding`: Additional size added to one side of the output shape
- `dilation`: Dilation of the convolution
- `groups`: The number of groups for the convolution
- `bias`: If `true` add a learnable bias to the output


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/convtransposed2d/init(inputchannels:outputchannels:kernelsize:stride:padding:outputpadding:dilation:groups:bias:))*