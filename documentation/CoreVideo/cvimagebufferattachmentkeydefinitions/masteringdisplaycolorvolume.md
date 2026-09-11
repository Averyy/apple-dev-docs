# masteringDisplayColorVolume

**Framework**: Core Video  
**Kind**: property

Mastering display color volume of the image.

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
static var masteringDisplayColorVolume: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data> { get }
```

#### Discussion

The value for this key is a 44 byte big-endian data sequence to match the payload of ISO/IEC 23008-2:2015(E), D.2.28 mastering display color volume in the supplemental enhancement information (SEI) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/masteringdisplaycolorvolume)*