# withPixelBufferIfAvailable(_:)

**Framework**: Core ML  
**Kind**: method

Reads the underlying pixel buffer.

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
func withPixelBufferIfAvailable<R>(_ body: (CVPixelBuffer) throws -> R) rethrows -> R?
```

#### Return Value

The value returned from body, unless the shaped array doesn’t use a pixel buffer backing, in which case the method ignores body and returns nil.

#### Discussion

Use this method to read the contents of the underlying pixel buffer. The pixel buffer is read only. Do not write to it.

```swift
let array = MLShapedArray<Float16>(mutating: pixelBuffer, shape: [2, 3])
array.withPixelBuffer { backingPixelBuffer in
     // read backingPixelBuffer here.
}
```

## Parameters

- `body`: The closure to run with the pixel buffer.

## See Also

- [func withMutablePixelBufferIfAvailable<R>((CVPixelBuffer) throws -> R) rethrows -> R?](mlshapedarray/withmutablepixelbufferifavailable(_:).md)
  Writes to the underlying pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/withpixelbufferifavailable(_:))*