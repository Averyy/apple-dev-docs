# textStylingResolution

**Framework**: AVFoundation  
**Kind**: property

A string identifier indicating the degree of text styling to be applied to attributed strings vended by the  object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var textStylingResolution: AVPlayerItemLegibleOutput.TextStylingResolution { get set }
```

#### Discussion

Valid values are described in `Text Style Settings`.  An exception ([`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception)) is raised if this property is set to any other value.

The default value is [`default`](avplayeritemlegibleoutput/textstylingresolution-swift.struct/default.md), which indicates that attributed strings vended by the receiver includes the same level of styling information that would be used if the text was rendered by an instance of [`AVPlayerLayer`](avplayerlayer.md).

> **Note**:  This is an advanced feature and you should rarely need to change it from the default value.

 This is an advanced feature and you should rarely need to change it from the default value.

## See Also

- [AVPlayerItemLegibleOutput.TextStylingResolution](avplayeritemlegibleoutput/textstylingresolution-swift.struct.md)
  A text styling resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.property)*