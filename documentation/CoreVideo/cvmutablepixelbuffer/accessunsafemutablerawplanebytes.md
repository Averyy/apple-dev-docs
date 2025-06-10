# accessUnsafeMutableRawPlaneBytes(_:)

**Framework**: Core Video  
**Kind**: method

Access the pixels in the planes contained within this buffer. The base address is locked for writing during the execution of the block.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func accessUnsafeMutableRawPlaneBytes<R>(_ block: ([(properties: CVPixelBufferPlaneProperties, bytes: UnsafeMutableRawBufferPointer)]) throws -> sending R) rethrows -> sending R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/accessunsafemutablerawplanebytes(_:))*