# BNNS.EmbeddingLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps an embedding filter and manages its deinitialization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
class EmbeddingLayer
```

#### Overview

Use an embedding layer to access dictionary items based on the integer indices that the input tensor defines.

For example, the following code shows how to access three dictionary items at indices `1`, `5`, and `2`. The dictionary contains seven items that are five-element vectors. Therefore, the indices descriptor has the shape `(3)`, the dictionary descriptor has the shape `(5, 7)`, and the output descriptor has the shape `(5, 3)`.

```swift
let lookupIndices: [Int8] = [1, 5, 2]
let input = BNNSNDArrayDescriptor.allocate(initializingFrom: lookupIndices,
                                           shape: .vector(lookupIndices.count))

// The dictionary contains 7 embeddings of 5-element vectors
let dictionaryData: [Float] = [ 01, 02, 03, 04, 05,     // Dictionary item 0
                                11, 12, 13, 14, 15,     // Dictionary item 1
                                21, 22, 23, 24, 25,     // Dictionary item 2
                                31, 32, 33, 34, 35,     // Dictionary item 3
                                41, 42, 43, 44, 45,     // Dictionary item 4
                                51, 52, 53, 54, 55,     // Dictionary item 5
                                61, 62, 63, 64, 65]     // Dictionary item 6

let dictionaryItemSize = 5
let dictionaryItemCount = 7

let dictionary = BNNSNDArrayDescriptor.allocate(
    initializingFrom: dictionaryData,
    shape: .matrixLastMajor(dictionaryItemSize,
                            dictionaryItemCount))

let output = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .matrixLastMajor(dictionaryItemSize,
                            lookupIndices.count))

let layer = BNNS.EmbeddingLayer(input: input,
                                output: output,
                                dictionary: dictionary,
                                paddingIndex: 0,
                                maximumNorm: 0,
                                normType: .euclidean,
                                scalesGradientByFrequency: false)

try? layer?.apply(batchSize: 1,
                  input: input,
                  output: output)

// Prints:
// [11.0, 12.0, 13.0, 14.0, 15.0,
// 51.0, 52.0, 53.0, 54.0, 55.0,
// 21.0, 22.0, 23.0, 24.0, 25.0]
print(output.makeArray(of: Float.self)!)

input.deallocate()
output.deallocate()
dictionary.deallocate()
```

The embedding layer supports clipping to a maximum norm. The following code accesses the second and third items from a dictionary that contains three 2 x 3 matrices. The code initializes the embedding layer with a maximum norm that is the infinity-norm of the first dictionary item.

```swift
let lookupIndices: [Int8] = [1, 2]
let input = BNNSNDArrayDescriptor.allocate(initializingFrom: lookupIndices,
                                           shape: .vector(lookupIndices.count))


// The dictionary contains 3 embeddings of 2 x 3 matrices.
let dictionaryData: [Float] = [0.1, 0.2, 0.3,
                               0.4, 0.5, 0.6,
                               
                               1, 3, 5,
                               2, 4, 6,
                               
                               60, 50, 40,
                               30, 20, 10]

let dictionaryItemRowCount = 2
let dictionaryItemColumnCount = 3
let dictionaryItemCount = 3

let dictionary = BNNSNDArrayDescriptor.allocate(
    initializingFrom: dictionaryData,
    shape: .tensor3DLastMajor(dictionaryItemRowCount,
                              dictionaryItemColumnCount,
                              dictionaryItemCount))

let output = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .tensor3DLastMajor(dictionaryItemRowCount,
                              dictionaryItemColumnCount,
                              lookupIndices.count))

let layer = BNNS.EmbeddingLayer(input: input,
                                output: output,
                                dictionary: dictionary,
                                paddingIndex: 0,
                                maximumNorm: 0.6,
                                normType: .lInfinity,
                                scalesGradientByFrequency: false)

try? layer?.apply(batchSize: 1,
                  input: input,
                  output: output)

// Prints:
// [0.1, 0.3, 0.5,
// 0.2, 0.4, 0.6,
//
// 0.6, 0.5, 0.4,
// 0.3, 0.2, 0.1]
print(output.makeArray(of: Float.self)!)

input.deallocate()
output.deallocate()
dictionary.deallocate()
```

## Topics

### Creating an Embedding Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, dictionary: BNNSNDArrayDescriptor, paddingIndex: Int, maximumNorm: Float, normType: BNNS.Norm, scalesGradientByFrequency: Bool, filterParameters: BNNSFilterParameters?)](bnns/embeddinglayer/init(input:output:dictionary:paddingindex:maximumnorm:normtype:scalesgradientbyfrequency:filterparameters:).md)
  Returns a new embedding layer.
- [struct Norm](bnns/norm.md)
  Constants that describe norm types.
### Applying an Embedding Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/embeddinglayer/apply(batchsize:input:output:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingWeightsGradient: BNNSNDArrayDescriptor) throws](bnns/embeddinglayer/applybackward(batchsize:input:output:outputgradient:generatingweightsgradient:).md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.Layer](bnns/layer.md)

## See Also

- [struct BNNSLayerParametersEmbedding](bnnslayerparametersembedding.md)
  A structure that contains the parameters of an embedding layer.
- [func BNNSFilterCreateLayerEmbedding(UnsafePointer<BNNSLayerParametersEmbedding>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerembedding(_:_:).md)
  Returns a new embedding layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/embeddinglayer)*