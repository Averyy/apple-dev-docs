# mediaSelectionGroup(forMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a media selection group that contains one or more options with the specified media characteristic.

**Availability**:
- iOS 5.0+ - Deprecated in 16.0
- iPadOS 5.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadMediaSelectionGroup(for:completionHandler:)`](./loadmediaselectiongroup%28for,completionhandler%29.md) instead.

## Declaration

```swift
func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?
```

```objc
- (AVMediaSelectionGroup *) mediaSelectionGroupForMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

## Mentions

- [Selecting subtitles and alternative audio tracks](../selecting-subtitles-and-alternative-audio-tracks.md)

#### Return Value

An [`AVMediaSelectionGroup`](../avmediaselectiongroup.md) that contains one or more options with the specified media characteristic, or `nil` if none could be found.

#### Discussion

Use the filtering methods [`AVMediaSelectionGroup`](../avmediaselectiongroup.md) defines to filter the group’s options according to playability, locale, and additional media characteristics.

You can call this method without blocking the current thread after you’ve asynchronously loaded the [`availableMediaCharacteristicsWithMediaSelectionOptions`](./availablemediacharacteristicswithmediaselectionoptions.md) property.

## Parameters

- `mediaCharacteristic`: A media characteristic for which to obtain the available media selection options.

  Only [`audible`](../avmediacharacteristic/audible.md), [`visual`](../avmediacharacteristic/visual.md), and [`legible`](../avmediacharacteristic/legible.md) are currently supported.

  - Pass [`audible`](../avmediacharacteristic/audible.md) to return the group of available options for audio media in various languages and for various purposes, such as descriptive audio.
  - Pass [`legible`](../avmediacharacteristic/legible.md) to return the group of available options for subtitles in various languages and for various purposes.
  - Pass [`visual`](../avmediacharacteristic/visual.md) to return the group of available options for video media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/mediaselectiongroup(formediacharacteristic:))*