# init(unsafeBuffer:)

**Framework**: Core Video  
**Kind**: init

Initialize a read-only pixel buffer by transferring existing CVPixelBuffer value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(unsafeBuffer: sending CVPixelBuffer)
```

## Parameters

- `unsafeBuffer`: Owership of this buffer is transferred to the new instance. This buffer is   copied   and must not be modified after this call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvreadonlypixelbuffer/init(unsafebuffer:))*