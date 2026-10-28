# hasMediaCharacteristic(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) hasMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

## Return Value

[`true`](../../Swift/true.md) if the media selection option has media with mediaCharacteristic, otherwise [`false`](../../Swift/false.md).

## Parameters

- `mediaCharacteristic`: The media characteristic of interest, for example, [`visual`](../avmediacharacteristic/visual.md), [`audible`](../avmediacharacteristic/audible.md), or [`legible`](../avmediacharacteristic/legible.md).

## See Also

### Accessing media information
- [var mediaType: AVMediaType](./mediatype.md)
  The media type of the media data.
- [var mediaSubTypes: [NSNumber]](./mediasubtypes.md)
  The media sub-types of the media data associated with the option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/hasmediacharacteristic(_:))*