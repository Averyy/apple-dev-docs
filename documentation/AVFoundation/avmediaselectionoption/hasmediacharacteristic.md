# hasMediaCharacteristic(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.

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
func hasMediaCharacteristic(_ mediaCharacteristic: AVMediaCharacteristic) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the media selection option has media with mediaCharacteristic, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `mediaCharacteristic`: The media characteristic of interest, for example,  ,  , or  .

## See Also

- [var mediaType: AVMediaType](avmediaselectionoption/mediatype.md)
  The media type of the media data.
- [var mediaSubTypes: [NSNumber]](avmediaselectionoption/mediasubtypes.md)
  The media sub-types of the media data associated with the option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/hasmediacharacteristic(_:))*