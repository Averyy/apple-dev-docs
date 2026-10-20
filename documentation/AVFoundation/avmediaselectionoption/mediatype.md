# mediaType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) AVMediaType mediaType;
```

#### Discussion

The value of the property might be, for example, [`audio`](../avmediatype/audio.md) or [`subtitle`](../avmediatype/subtitle.md).

## See Also

### Accessing media information
- [var mediaSubTypes: [NSNumber]](./mediasubtypes.md)
  The media sub-types of the media data associated with the option.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](./hasmediacharacteristic%28_%29.md)
  Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/mediatype)*