# mediaSubTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * mediaSubTypes;
```

#### Discussion

The value is an array of `NSNumber` objects carrying four character codes (of type FourCharCode) as defined in `CoreAudioTypes.h` for audio media and in `CMFormatDescription.h` for video media.

Also see [`CMFormatDescriptionGetMediaSubType(_:)`](../../CoreMedia/cmformatdescriptiongetmediasubtype%28_%29.md) for more information about media subtypes.

## See Also

### Accessing media information
- [var mediaType: AVMediaType](./mediatype.md)
  The media type of the media data.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](./hasmediacharacteristic%28_%29.md)
  Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/mediasubtypes)*