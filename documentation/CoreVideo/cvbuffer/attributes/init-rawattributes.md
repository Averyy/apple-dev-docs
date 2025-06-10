# init(rawAttributes:)

**Framework**: Core Video  
**Kind**: init

Create an instance using a freeform attribute dictionary

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)
- Unknown ?+ - Deprecated
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
init(rawAttributes: [String : any Sendable])
```

#### Discussion

This dictionary should only contain the pixel buffer attributes that [`CVPixelBufferCreate(_:_:_:_:_:_:)`](cvpixelbuffercreate(_:_:_:_:_:_:).md) function accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer/attributes/init(rawattributes:))*