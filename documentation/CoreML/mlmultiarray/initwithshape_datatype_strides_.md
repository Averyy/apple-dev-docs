# initWithShape:dataType:strides:

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Creates the object with specified strides.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
- (instancetype) initWithShape:(NSArray<NSNumber *> *) shape dataType:(MLMultiArrayDataType) dataType strides:(NSArray<NSNumber *> *) strides;
```

#### Discussion

The contents of the object are left uninitialized; the client must initialize it.

```swift
let shape = [2, 3];
let strides = [4, 1]

let multiArray = MLMultiArray(shape: shape, dataType: .float32, strides: strides)
XCTAssertEqual(multiArray.shape, shape as [NSNumber])
XCTAssertEqual(multiArray.strides, strides as [NSNumber])
```

```objc
NSArray<NSNumber *> *shape = @[@2, @3];
NSArray<NSNumber *> *strides = @[@4, @1];

MLMultiArray *multiArray = [[MLMultiArray alloc] initWithShape:shape
                                                      dataType:MLMultiArrayDataTypeFloat32
                                                       strides:strides];
XCTAssertEqualObjects(multiArray.shape, shape);
XCTAssertEqualObjects(multiArray.strides, strides);
```

## Parameters

- `shape`: The shape
- `dataType`: The data type
- `strides`: The strides.

## See Also

### Creating a multiarray
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](./init%28shape,datatype%29.md)
  Creates a multidimensional array with a shape and type.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](./init%28datapointer,shape,datatype,strides,deallocator%29.md)
  Creates a multiarray from a data pointer.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](./init%28pixelbuffer,shape%29.md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/initwithshape:datatype:strides:)*