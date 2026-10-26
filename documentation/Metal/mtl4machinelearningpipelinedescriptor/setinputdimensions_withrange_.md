# setInputDimensions:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets the dimensions of multiple input tensors on a range of buffer bindings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) setInputDimensions:(NSArray<MTLTensorExtents *> *) dimensions withRange:(NSRange) range;
```

#### Discussion

Use this method to specify the dimensions of multiple input tensors at a range of indices in a single call.

You can indicate that any tensors in the range have unspecified dimensions by providing `NSNull` at the their corresponding index location in the array.

> ❗ **Important**: The range’s length property needs to match the number of dimensions you provide. Specifically, `range.length` needs to match `dimensions.count`.

## Parameters

- `dimensions`: An array of tensor extents.
- `range`: The range of inputs of the `dimensions` argument. The range’s `length` needs to match the dimensions’ `count` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions:withrange:)*