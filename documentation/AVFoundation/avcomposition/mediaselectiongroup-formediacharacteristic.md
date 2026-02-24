# mediaSelectionGroup(forMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

Returns a media selection group that contains one or more options with the specified media characteristic.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?
```

#### Return Value

An [`AVMediaSelectionGroup`](avmediaselectiongroup.md) that contains one or more options with the specified media characteristic, or `nil` if none could be found.

#### Discussion

Use the filtering methods [`AVMediaSelectionGroup`](avmediaselectiongroup.md) defines to filter the group’s options according to playability, locale, and additional media characteristics.

You can call this method without blocking the current thread after you’ve asynchronously loaded the [`availableMediaCharacteristicsWithMediaSelectionOptions`](avasset/availablemediacharacteristicswithmediaselectionoptions.md) property.

## Parameters

- `mediaCharacteristic`: A media characteristic for which to obtain the available media selection options. Only [`audible`](avmediacharacteristic/audible.md), [`visual`](avmediacharacteristic/visual.md), and [`legible`](avmediacharacteristic/legible.md) are currently supported. - Pass [`audible`](avmediacharacteristic/audible.md) to return the group of available options for audio media in various languages and for various purposes, such as descriptive audio.
- Pass [`legible`](avmediacharacteristic/legible.md) to return the group of available options for subtitles in various languages and for various purposes.
- Pass [`visual`](avmediacharacteristic/visual.md) to return the group of available options for video media.

## See Also

- [var allMediaSelections: [AVMediaSelection]](avcomposition/allmediaselections.md)
  The array of available media selections for this asset.
- [var availableMediaCharacteristicsWithMediaSelectionOptions: [AVMediaCharacteristic]](avcomposition/availablemediacharacteristicswithmediaselectionoptions.md)
  An array of media characteristics for which a media selection option is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/mediaselectiongroup(formediacharacteristic:))*