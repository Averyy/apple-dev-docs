# BNNSTensor

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSTensor
```

```c
typedef struct { ... } BNNSTensor;
```

## Topics

### Initializers
- [init()](./bnnstensor/init%28%29.md)
  Creates an empty tensor.
- [init(data_type: BNNSDataType, rank: UInt8, shape: (Int, Int, Int, Int, Int, Int, Int, Int), stride: (Int, Int, Int, Int, Int, Int, Int, Int), data: UnsafeMutableRawPointer?, data_size_in_bytes: Int, name: UnsafePointer<CChar>?)](./bnnstensor/init%28data_type,rank,shape,stride,data,data_size_in_bytes,name%29.md)
  Creates a tensor with the specified properties.
- [init<T>(data: UnsafeMutableBufferPointer<T>, shape: [Int], stride: [Int])](./bnnstensor/init%28data,shape,stride%29.md)
  Creates a `BNNSTensor` that references the same memory as the specified `UnsafeMutableBufferPointer`.
- [init(data: UnsafeMutableRawBufferPointer, shape: [Int], stride: [Int], dataType: BNNSDataType)](./bnnstensor/init%28data,shape,stride,datatype%29.md)
  Creates a `BNNSTensor` that references the same memory as the specified `UnsafeMutableRawBufferPointer`.
- [init(dataType: BNNSDataType, shape: [Int], stride: [Int])](./bnnstensor/init%28datatype,shape,stride%29.md)
  Creates an unallocated `BNNSTensor`
- [init<T>(initializingFrom: some AccelerateBuffer, shape: [Int], stride: [Int])](./bnnstensor/init%28initializingfrom,shape,stride%29.md)
  Returns a `BNNSTensor` structure that’s initialized with every element of the source.
- [init(shape: [Int], stride: [Int], dataType: BNNSDataType)](./bnnstensor/init%28shape,stride,datatype%29.md)
  Returns a `BNNSTensor` structure based on the supplied shape and data type.
### Specifying a tensor’s properties
- [var data_type: BNNSDataType](./bnnstensor/data_type.md)
  The data type of the tensor.
- [var rank: UInt8](./bnnstensor/rank.md)
  The rank of the tensor.
- [var shape: (Int, Int, Int, Int, Int, Int, Int, Int)](./bnnstensor/shape.md)
  A tuple of unsigned-integer elements that specify the size of the tensor.
- [var stride: (Int, Int, Int, Int, Int, Int, Int, Int)](./bnnstensor/stride.md)
  A tuple of unsigned-integer elements that specify the stride of the tensor.
- [var data: UnsafeMutableRawPointer?](./bnnstensor/data.md)
  A pointer to the memory that contains the tensor values.
- [var data_size_in_bytes: Int](./bnnstensor/data_size_in_bytes.md)
  The size, in bytes, of the memory that contains the tensor values.
- [var name: UnsafePointer<CChar>?](./bnnstensor/name.md)
  An optional name for the tensor that you can use for debugging.
### Instance Properties
- [var count: Int](./bnnstensor/count.md)
  The number of elements in the tensor.
### Instance Methods
- [func allocate<T>(as: T.Type, count: Int)](./bnnstensor/allocate%28as,count%29.md)
  Allocates a tensor with existing size and stride populated by `Context.tensor(forFunction:argument:fillKnownDynamicShapes:)`.
- [func allocate<T>(initializingFrom: some AccelerateBuffer)](./bnnstensor/allocate%28initializingfrom%29.md)
  Allocates and initializes a tensor with existing size and stride populated by `Context.tensor(forFunction:argument:fillKnownDynamicShapes:)`.
- [func deallocate()](./bnnstensor/deallocate%28%29.md)
  Deallocates the previously allocated memory block referenced by this pointer.
- [func makeArray<T>(of: T.Type) -> [T]](./bnnstensor/makearray%28of%29.md)
  Returns an array that contains a copy of this `BNNSTensor`’s elements.
### Type Methods
- [static func allocate<C>(initializingFrom: C, shape: [Int], stride: [Int]) -> BNNSTensor](./bnnstensor/allocate%28initializingfrom,shape,stride%29.md)
  Creates a `BNNSTensor` populated with a **copy** of the values in `source`.
- [static func allocate<T>(repeating: T, shape: [Int], stride: [Int]) -> BNNSTensor](./bnnstensor/allocate%28repeating,shape,stride%29.md)
  Creates a `BNNSTensor` filled with the specified scalar value.
- [static func allocateUninitialized(scalarType: any BNNSScalar.Type, shape: [Int], stride: [Int]) -> BNNSTensor](./bnnstensor/allocateuninitialized%28scalartype,shape,stride%29.md)
  Creates a `BNNSTensor` of the specified data type with allocated memory.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Specifying and querying a tensor’s properties
- [func BNNSTensorGetAllocationSize(UnsafePointer<BNNSTensor>) -> Int](./bnnstensorgetallocationsize%28_%29.md)
  Returns the minimum allocation size, in bytes, of the specified tensor.
- [func BNNSGraphContextGetTensor(bnns_graph_context_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, Bool, UnsafeMutablePointer<BNNSTensor>) -> Int32](./bnnsgraphcontextgettensor%28_,_,_,_,_%29.md)
  Sets the properties of a tensor for the specified function argument.
- [func BNNSGraphTensorFillStrides(bnns_graph_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, UnsafeMutablePointer<BNNSTensor>) -> Int32](./bnnsgraphtensorfillstrides%28_,_,_,_%29.md)
  Sets the stride of the specifed tensor for compatibility with the given model’s input or output argument based on its current shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensor)*