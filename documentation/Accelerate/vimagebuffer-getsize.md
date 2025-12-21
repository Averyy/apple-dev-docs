# vImageBuffer_GetSize(_:)

**Framework**: Accelerate  
**Kind**: func

Returns the size, in pixels, of a vImage buffer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageBuffer_GetSize(_ buf: UnsafePointer<vImage_Buffer>) -> CGSize
```

#### Return Value

The size of the buffer.

#### Discussion

The vImage library defines a buffer’s width and height as [`vImagePixelCount`](vimagepixelcount.md) values that may be larger than [`greatestFiniteMagnitude`](https://developer.apple.com/documentation/Swift/FloatingPoint/greatestFiniteMagnitude). This function rounds down the buffer’s dimensions to the nearest representable [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) values that are less than, or equal to, the size of the buffer.

## Parameters

- `buf`: The vImage buffer to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebuffer_getsize(_:))*