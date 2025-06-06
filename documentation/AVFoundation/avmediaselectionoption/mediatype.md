# mediaType

**Framework**: AVFoundation  
**Kind**: property

The media type of the media data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var mediaType: AVMediaType { get }
```

#### Discussion

The value of the property might be, for example, [`audio`](avmediatype/audio.md) or [`subtitle`](avmediatype/subtitle.md).

## See Also

- [var mediaSubTypes: [NSNumber]](avmediaselectionoption/mediasubtypes.md)
  The media sub-types of the media data associated with the option.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avmediaselectionoption/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/mediatype)*