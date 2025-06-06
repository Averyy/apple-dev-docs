# mediaSubTypes

**Framework**: AVFoundation  
**Kind**: property

The media sub-types of the media data associated with the option.

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
var mediaSubTypes: [NSNumber] { get }
```

#### Discussion

The value is an array of `NSNumber` objects carrying four character codes (of type FourCharCode) as defined in `CoreAudioTypes.h` for audio media and in `CMFormatDescription.h` for video media.

Also see [`CMFormatDescriptionGetMediaSubType(_:)`](https://developer.apple.com/documentation/CoreMedia/CMFormatDescriptionGetMediaSubType(_:)) for more information about media subtypes.

## See Also

- [var mediaType: AVMediaType](avmediaselectionoption/mediatype.md)
  The media type of the media data.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avmediaselectionoption/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/mediasubtypes)*