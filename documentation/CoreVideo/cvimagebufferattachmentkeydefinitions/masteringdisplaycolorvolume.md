# masteringDisplayColorVolume

**Framework**: Core Video  
**Kind**: property

Mastering display color volume of the image.

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
static var masteringDisplayColorVolume: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data> { get }
```

#### Discussion

The value for this key is a 44 byte big-endian data sequence to match the payload of ISO/IEC 23008-2:2015(E), D.2.28 mastering display color volume in the supplemental enhancement information (SEI) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/masteringdisplaycolorvolume)*