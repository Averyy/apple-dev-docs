# ambientViewingEnvironment

**Framework**: Core Video  
**Kind**: property

The ambient viewing environment for the image. The value for this key is an 8 byte big-endian data sequence to match the payload of the Ambient Viewing Environment SEI message.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var ambientViewingEnvironment: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data> { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/ambientviewingenvironment)*