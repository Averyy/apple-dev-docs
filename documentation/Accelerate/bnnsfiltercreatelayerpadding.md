# BNNSFilterCreateLayerPadding(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new loss layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSFilterCreateLayerPadding(_ layer_params: UnsafePointer<BNNSLayerParametersPadding>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

Use a padding layer to add elements to an n-dimensional array before and after existing data. The padding can either contain a single value or a reflection of the existing data. For `BNNSPaddingModeConstant`, pass the bit pattern of the padding value, for example, using [`bitPattern`](https://developer.apple.com/documentation/Swift/Float/bitPattern) to pass a single-precision value.

The following code shows how to add two elements before, and four elements after a vector of ten values:

```swift
let paddingSize = (2, 4)

let source: [Float] = [ 0, 1, 2, 3, 4, 5, 7, 8, 9 ]

var destination = [Float](repeating: 0,
                          count: source.count + paddingSize.0 + paddingSize.1)

let srcDescription = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                           layout: BNNSDataLayoutVector,
                                           size: (source.count, 0, 0, 0, 0, 0, 0, 0),
                                           stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                           data: nil,
                                           data_type: .float,
                                           table_data: nil,
                                           table_data_type: .float,
                                           data_scale: 1,
                                           data_bias: 0)

let destDescription = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                            layout: BNNSDataLayoutVector,
                                            size: (destination.count, 0, 0, 0, 0, 0, 0, 0),
                                            stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                            data: nil,
                                            data_type: .float,
                                            table_data: nil,
                                            table_data_type: .float,
                                            data_scale: 1,
                                            data_bias: 0)

let paddingValue: Float = 99

var parameters = BNNSLayerParametersPadding(i_desc: srcDescription,
                                            o_desc: destDescription,
                                            padding_size: (paddingSize, (0, 0), (0, 0), (0, 0),
                                                           (0, 0), (0, 0), (0, 0), (0, 0)),
                                            padding_mode: BNNSPaddingModeConstant,
                                            padding_value: paddingValue.bitPattern)

var filterParams = BNNSFilterParameters()

let filter = BNNSFilterCreateLayerPadding(&parameters, &filterParams)
defer {
    BNNSFilterDestroy(filter)
}

BNNSFilterApply(filter,
                source,
                &destination)
```

On return, `destination` contains `[99.0, 99.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0, 8.0, 9.0, 99.0, 99.0, 99.0, 99.0]`.

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

- [class PaddingLayer](bnns/paddinglayer.md)
  A layer object that wraps a padding filter and manages its deinitialization.
- [struct BNNSPaddingMode](bnnspaddingmode.md)
  Constants that define padding modes.
- [struct BNNSLayerParametersPadding](bnnslayerparameterspadding.md)
  A structure that contains the parameters of a padding layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayerpadding(_:_:))*