# mediaSelectionCriteria(forMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

Returns the automatic selection criteria for media items with the specified media characteristic.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func mediaSelectionCriteria(forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> AVPlayerMediaSelectionCriteria?
```

#### Return Value

The [`AVPlayerMediaSelectionCriteria`](avplayermediaselectioncriteria.md) for `mediaCharacteristic`.

## Parameters

- `mediaCharacteristic`: The media characteristic for which the selection criteria is to be returned. Supported values include  ,  , and  .

## See Also

- [var appliesMediaSelectionCriteriaAutomatically: Bool](avplayer/appliesmediaselectioncriteriaautomatically.md)
  A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.
- [func setMediaSelectionCriteria(AVPlayerMediaSelectionCriteria?, forMediaCharacteristic: AVMediaCharacteristic)](avplayer/setmediaselectioncriteria(_:formediacharacteristic:).md)
  Applies automatic selection criteria for media that has the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/mediaselectioncriteria(formediacharacteristic:))*