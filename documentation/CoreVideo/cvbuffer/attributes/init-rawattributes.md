# init(rawAttributes:)

**Framework**: Core Video  
**Kind**: init

Create an instance using a freeform attribute dictionary

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
init(rawAttributes: [String : any Sendable])
```

#### Discussion

This dictionary should only contain the pixel buffer attributes that [`CVPixelBufferCreate(_:_:_:_:_:_:)`](cvpixelbuffercreate(_:_:_:_:_:_:).md) function accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer/attributes/init(rawattributes:))*