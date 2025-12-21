# withMutablePixelBufferIfAvailable(_:)

**Framework**: Core ML  
**Kind**: method

Writes to the underlying pixel buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
mutating func withMutablePixelBufferIfAvailable<R>(_ body: (CVPixelBuffer) throws -> R) rethrows -> R?
```

#### Discussion

Use this method to writes the contents of the underlying pixel buffer.

```swift
let array = MLShapedArray<Float16>(mutating: pixelBuffer, shape: [2, 3])
array.withMutablePixelBuffer { backingPixelBuffer in
     // write backingPixelBuffer here.
}
```

## Parameters

- `body`: The closure to run with the pixel buffer.

## See Also

- [func withPixelBufferIfAvailable<R>((CVPixelBuffer) throws -> R) rethrows -> R?](mlshapedarray/withpixelbufferifavailable(_:).md)
  Reads the underlying pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/withmutablepixelbufferifavailable(_:))*