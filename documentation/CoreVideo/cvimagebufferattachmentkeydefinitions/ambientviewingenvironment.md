# ambientViewingEnvironment

**Framework**: Core Video  
**Kind**: property

The ambient viewing environment for the image. The value for this key is an 8 byte big-endian data sequence to match the payload of the Ambient Viewing Environment SEI message.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var ambientViewingEnvironment: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data> { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/ambientviewingenvironment)*