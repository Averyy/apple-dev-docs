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

- `mediaCharacteristic`: Only  ,  , and   are currently supported.

## See Also

- [var allMediaSelections: [AVMediaSelection]](avcomposition/allmediaselections.md)
  The array of available media selections for this asset.
- [var availableMediaCharacteristicsWithMediaSelectionOptions: [AVMediaCharacteristic]](avcomposition/availablemediacharacteristicswithmediaselectionoptions.md)
  An array of media characteristics for which a media selection option is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/mediaselectiongroup(formediacharacteristic:))*