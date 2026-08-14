# init(shape:dataType:)

**Framework**: Core ML  
**Kind**: init

Creates a multidimensional array with a shape and type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws
```

#### Discussion

This method allocates a contiguous region of memory for the multiarray’s shape. You must set the contents of memory. The multiarray frees the memory in its deinitializer (Swift) or [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/dealloc) method (Objective-C).

The following code creates a 3 x 3 multiarray and sets its contents to the value 3.14159.

**Swift**:

```swift
// Create a 2D multiarray with dimension 3 x 3.
let shape3x3 = [3, 3] as [NSNumber]

guard let multiarray3x3 = try? MLMultiArray(shape: shape3x3, dataType: .float) else {
    // Handle the error.
    return
}

print("Before: \(multiarray3x3)")

// Initialize the multiarray.
for xCoordinate in 0..<3 {
    for yCoordinate in 0..<3 {
        let key = [xCoordinate, yCoordinate] as [NSNumber]
        multiarray3x3[key] = 3.141_59
    }
}

print("After: \(multiarray3x3)")

```

**Objective-C**:

```objc
NSError *error = nil;

// Create a 2D multiarray with dimension 3 x 3.
NSArray<NSNumber *> *shape3x3 = @[@3, @3];

MLMultiArray *multiarray3x3 = [[MLMultiArray alloc] initWithShape:shape3x3 dataType:MLMultiArrayDataTypeFloat error: &error];
if (error != nil) {
    // Handle the error.
    return;
}

NSLog(@"Before: %@\n", multiarray3x3);

// Initialize the multiarray.
for (int x = 0; x < 3; x++) {
    for (int y = 0; y < 3; y++) {
        NSNumber *xSubscript = [NSNumber numberWithInt:x];
        NSNumber *ySubscript = [NSNumber numberWithInt:y];

        [multiarray3x3 setObject:@3.14159
               forKeyedSubscript:@[xSubscript, ySubscript]];
    }
}

NSLog(@"After: %@\n", multiarray3x3);

```

## Parameters

- `shape`: An integer array that has an element for each dimension in a multiarray that represents its length.
- `dataType`: An element type defined by [`MLMultiArrayDataType`](mlmultiarraydatatype.md).

## See Also

- [convenience(_:)](mlmultiarray/init(_:).md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](mlmultiarray/init(shape:datatype:strides:).md)
  Creates the object with specified strides.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](mlmultiarray/init(datapointer:shape:datatype:strides:deallocator:).md)
  Creates a multiarray from a data pointer.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](mlmultiarray/init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(shape:datatype:))*