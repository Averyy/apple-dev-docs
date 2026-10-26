---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/convtransposed1d/init(inputchannels:outputchannels:kernelsize:stride:padding:outputpadding:dilation:groups:bias:)"
framework: "mlx-swift/MLXNN"
---

# init(inputChannels:outputChannels:kernelSize:stride:padding:outputPadding:dilation:groups:bias:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies a 1-dimensional transposed convolution over the multi-channel input sequence.

## Declaration

```swift
init(inputChannels: Int, outputChannels: Int, kernelSize: Int, stride: Int = 1, padding: Int = 0, outputPadding: Int = 0, dilation: Int = 1, groups: Int = 1, bias: Bool = true)
```

#### Discussion

The channels are expected to be last i.e. the input shape should be `NLC` where:

- `N` is the batch dimension
- `L` is the sequence length
- `C` is the number of input channels

## Parameters

- `inputChannels`: Number of input channels (`C` from the discussion)
- `outputChannels`: Number of output channels
- `kernelSize`: Size of the convolution filters
- `stride`: Stride when applying the filter
- `padding`: How many positions to 0-pad the input with
- `outputPadding`: Additional size added to one size of the output shape
- `dilation`: Dilation of the convolution
- `groups`: The number of groups for the convolution
- `bias`: If `true` add a learnable bias to the output


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/convtransposed1d/init(inputchannels:outputchannels:kernelsize:stride:padding:outputpadding:dilation:groups:bias:))*