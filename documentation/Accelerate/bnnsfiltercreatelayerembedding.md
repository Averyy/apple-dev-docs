# BNNSFilterCreateLayerEmbedding(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new embedding layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func BNNSFilterCreateLayerEmbedding(_ layer_params: UnsafePointer<BNNSLayerParametersEmbedding>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

Use this function in conjunction with [`BNNSLayerParametersEmbedding`](bnnslayerparametersembedding.md) to create an embedding layer that accesses dictionary items based on the integer indices that the input tensor defines.

For example, the following code shows how to access three dictionary items at indices `1`, `5`, and `2`. The dictionary contains seven items that are five-element vectors. Therefore, the indices descriptor has the shape `(3)`, the dictionary descriptor has the shape `(5, 7)`, and the output descriptor has the shape `(5, 3)`.

```swift
static func embeddingLayer() {
    
    let indicesData = UnsafeMutableBufferPointer<Int8>.allocate(capacity: 3)
    _ = indicesData.initialize(from: [1, 5, 2])
    let indicesDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                  layout: BNNSDataLayoutVector,
                                                  size: (3, 0, 0, 0, 0, 0, 0, 0),
                                                  stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                  data: indicesData.baseAddress!,
                                                  data_type: BNNSDataType.int8,
                                                  table_data: nil,
                                                  table_data_type: BNNSDataType.int8,
                                                  data_scale: 1, data_bias: 0)
    
    let dictionaryItemSize = 5
    let dictionaryItemCount = 7
    let dictionaryData = UnsafeMutableBufferPointer<Float>.allocate(capacity: dictionaryItemSize * dictionaryItemCount)
    _ = dictionaryData.initialize(from: [01, 02, 03, 04, 05,
                                         11, 12, 13, 14, 15,
                                         21, 22, 23, 24, 25,
                                         31, 32, 33, 34, 35,
                                         41, 42, 43, 44, 45,
                                         51, 52, 53, 54, 55,
                                         61, 62, 63, 64, 65])
    let dictionaryDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                     layout: BNNSDataLayout2DLastMajor,
                                                     size: (dictionaryItemSize, dictionaryItemCount,
                                                            0, 0, 0, 0, 0, 0),
                                                     stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                     data: dictionaryData.baseAddress!,
                                                     data_type: BNNSDataType.float,
                                                     table_data: nil,
                                                     table_data_type: BNNSDataType.float,
                                                     data_scale: 1, data_bias: 0)
    
    let outputData = UnsafeMutableBufferPointer<Float>.allocate(capacity: dictionaryItemSize * indicesData.count)
    let outputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                 layout: BNNSDataLayout2DLastMajor,
                                                 size: (dictionaryItemSize, indicesData.count,
                                                        0, 0, 0, 0, 0, 0),
                                                 stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                 data: outputData.baseAddress!,
                                                 data_type: BNNSDataType.float,
                                                 table_data: nil,
                                                 table_data_type: BNNSDataType.float,
                                                 data_scale: 1, data_bias: 0)
    
    var parameters = BNNSLayerParametersEmbedding(flags: BNNSEmbeddingFlags(rawValue: 0),
                                                  i_desc: indicesDescriptor,
                                                  o_desc: outputDescriptor,
                                                  dictionary: dictionaryDescriptor,
                                                  padding_idx: 0,
                                                  max_norm: 0,
                                                  norm_type: 0)
    
    let embeddingLayer = BNNSFilterCreateLayerEmbedding(&parameters, nil)
    
    BNNSFilterApply(embeddingLayer,
                    indicesDescriptor.data!,
                    outputDescriptor.data!)
    
    // Prints:
    // [11.0, 12.0, 13.0, 14.0, 15.0,
    //  51.0, 52.0, 53.0, 54.0, 55.0,
    //  21.0, 22.0, 23.0, 24.0, 25.0]
    print(Array(outputData))
    
    indicesData.deallocate()
    dictionaryData.deallocate()
    outputData.deallocate()
}
```

The embedding layer supports clipping to a maximum norm. The following code accesses the second and third items from a dictionary that contains three 2 x 3 matrices. The code initializes the embedding layer with a maximum norm that is the infinity-norm of the first dictionary item.

```swift
static func embeddingLayerClipByNorm() {
    let indicesData = UnsafeMutableBufferPointer<Int8>.allocate(capacity: 2)
    _ = indicesData.initialize(from: [1, 2])
    let indicesDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                  layout: BNNSDataLayoutVector,
                                                  size: (2, 0, 0, 0, 0, 0, 0, 0),
                                                  stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                  data: indicesData.baseAddress!,
                                                  data_type: BNNSDataType.int8,
                                                  table_data: nil,
                                                  table_data_type: BNNSDataType.float,
                                                  data_scale: 1, data_bias: 0)
    
    let dictionaryItemRowCount = 2
    let dictionaryItemColumnCount = 3
    let dictionaryItemCount = 3
    let dictionaryElementCount = dictionaryItemRowCount * dictionaryItemColumnCount * dictionaryItemCount
    let dictionaryData = UnsafeMutableBufferPointer<Float>.allocate(capacity: dictionaryElementCount)
    _ = dictionaryData.initialize(from: [0.1, 0.2, 0.3,
                                         0.4, 0.5, 0.6,
                                       
                                         1, 3, 5,
                                         2, 4, 6,
                                         
                                         60, 50, 40,
                                         30, 20, 10])
    let dictionaryDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                     layout: BNNSDataLayout3DLastMajor,
                                                     size: (dictionaryItemRowCount,
                                                            dictionaryItemColumnCount,
                                                            dictionaryItemCount, 0, 0, 0, 0, 0),
                                                     stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                     data: dictionaryData.baseAddress!,
                                                     data_type: BNNSDataType.float,
                                                     table_data: nil,
                                                     table_data_type: BNNSDataType.float,
                                                     data_scale: 1, data_bias: 0)
    
    let outputElementCount = dictionaryItemRowCount * dictionaryItemColumnCount * indicesData.count
    let outputData = UnsafeMutableBufferPointer<Float>.allocate(capacity: outputElementCount)
    let outputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                 layout: BNNSDataLayout3DLastMajor,
                                                 size: (dictionaryItemRowCount,
                                                        dictionaryItemColumnCount,
                                                        indicesData.count, 0, 0, 0, 0, 0),
                                                 stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                 data: outputData.baseAddress!,
                                                 data_type: BNNSDataType.float,
                                                 table_data: nil,
                                                 table_data_type: BNNSDataType.float,
                                                 data_scale: 1, data_bias: 0)
    
    var parameters = BNNSLayerParametersEmbedding(flags: BNNSEmbeddingFlags(rawValue: 0),
                                                  i_desc: indicesDescriptor,
                                                  o_desc: outputDescriptor,
                                                  dictionary: dictionaryDescriptor,
                                                  padding_idx: 0,
                                                  max_norm: 0.6,
                                                  norm_type: .infinity)
    
    let embeddingLayer = BNNSFilterCreateLayerEmbedding(&parameters, nil)
    
    BNNSFilterApply(embeddingLayer,
                    indicesDescriptor.data!,
                    outputDescriptor.data!)
    
    // Prints:
    //     [0.1, 0.3, 0.5,
    //      0.2, 0.4, 0.6,
    //
    //      0.6, 0.5, 0.4,
    //      0.3, 0.2, 0.1]
    print(Array(outputData))
    
    indicesData.deallocate()
    dictionaryData.deallocate()
    outputData.deallocate()
}
```

## Parameters

- `layer_params`: The layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

- [class EmbeddingLayer](bnns/embeddinglayer.md)
  A layer object that wraps an embedding filter and manages its deinitialization.
- [struct BNNSLayerParametersEmbedding](bnnslayerparametersembedding.md)
  A structure that contains the parameters of an embedding layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayerembedding(_:_:))*