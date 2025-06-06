# mediaSelectionGroup(forMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

Returns a media selection group that contains one or more options with the specified media characteristic.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?
```

## Mentions

- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)

#### Return Value

An [`AVMediaSelectionGroup`](avmediaselectiongroup.md) that contains one or more options with the specified media characteristic, or `nil` if none could be found.

#### Discussion

Use the filtering methods [`AVMediaSelectionGroup`](avmediaselectiongroup.md) defines to filter the group’s options according to playability, locale, and additional media characteristics.

You can call this method without blocking the current thread after you’ve asynchronously loaded the [`availableMediaCharacteristicsWithMediaSelectionOptions`](avasset/availablemediacharacteristicswithmediaselectionoptions.md) property.

## Parameters

- `mediaCharacteristic`: Only  ,  , and   are currently supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/mediaselectiongroup(formediacharacteristic:))*