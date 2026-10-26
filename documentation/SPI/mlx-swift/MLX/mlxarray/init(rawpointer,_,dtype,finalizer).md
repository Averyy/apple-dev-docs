---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(rawpointer:_:dtype:finalizer:)"
framework: "mlx-swift/MLX"
---

# init(rawPointer:_:dtype:finalizer:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initialize an MLXArray by transferring ownership of a raw pointer.

## Declaration

```swift
convenience init(rawPointer: UnsafeMutableRawPointer, _ shape: (some Collection<Int>)? = [Int]?.none, dtype: DType, finalizer: @escaping () -> Void)
```

#### Discussion

Note: the raw pointer must be compatible with the computational backing, e.g. a Metal stream requires something compatible with an `MTLBuffer`.

For example:

```swift
let height = 100
let width = 128
let pixelFormat = kCVPixelFormatType_32BGRA

let properties: [IOSurfacePropertyKey: any Sendable] = [
    .width: width,
    .height: height,
    .pixelFormat: pixelFormat,
    .bytesPerElement: 4
]

guard let ioSurface = IOSurface(properties: properties) else {
    XCTFail("unable to allocate IOSurface")
    return
}

let array = MLXArray(rawPointer: ioSurface.baseAddress, [height, width, 4] ,dtype: .uint8) {
    [ioSurface] in
    // this holds reference to the ioSurface and implicitly releases it when it returns
    _ = ioSurface
    print("release IOSurface")
}
```

## Parameters

- `rawPointer`: Raw pointer to input data – ownership is transferred to MLXArray.  The data must be contiguous in the shape and dtype given (or at least it will be treated as such)
- `shape`: Shape of the data in the rawPointer
- `dtype`: Data type
- `finalizer`: Closure that will release the associated resource


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(rawpointer:_:dtype:finalizer:))*