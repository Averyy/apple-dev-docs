# transfer(to:)

**Framework**: Core ML  
**Kind**: method

Transfer the contents to the destination multi-array.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func transfer(to destinationMultiArray: MLMultiArray)
```

#### Discussion

Numeric data will be up or down casted as needed. It can transfer to a multi-array with different layout (strides).

```swift
let sourceMultiArray: MLMultiArray = ... // shape is [2, 3] and data type is Float64

let newStrides = [4, 1]
let destinationMultiArray = MLMultiArray(shape: [2, 3], 
                                         dataType: .float32, 
                                         strides: newStrides)
sourceMultiArray.transfer(to: destinationMultiArray)
```

```objc
NSArray<NSNumber *> *shape = @[@2, @3];
NSArray<NSNumber *> *sourceStrides = @[@3, @1];
NSArray<NSNumber *> *destinationStrides = @[@4, @1];
MLMultiArray *source = [[MLMultiArray alloc] initWithShape:shape
                                                  dataType:MLMultiArrayDataTypeDouble
                                                   strides:sourceStrides];
// Initialize source...

MLMultiArray *destination = [[MLMultiArray alloc] initWithShape:shape
                                                       dataType:MLMultiArrayDataTypeFloat32
                                                        strides:destinationStrides];
[source transferToMultiArray:destination];
```

## Parameters

- `destinationMultiArray`: The transfer destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/transfer(to:))*