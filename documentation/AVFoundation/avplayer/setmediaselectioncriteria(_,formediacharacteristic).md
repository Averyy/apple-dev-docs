# setMediaSelectionCriteria(_:forMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Applies automatic selection criteria for media that has the specified media characteristic.

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
func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic)
```

```objc
- (void) setMediaSelectionCriteria:(AVPlayerMediaSelectionCriteria *) criteria forMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

## Discussion

Criteria will be applied to an [`AVPlayerItem`](../avplayeritem.md) instance when:

- It is made ready to play.
- Specific media selections are made by the [`AVPlayerItem`](../avplayeritem.md) instance using the method [`select(_:in:)`](../avplayeritem/select%28_,in%29.md) in a different group. The automatic choice in one group may be influenced by a specific selection in another group.
- Underlying system preferences change, e.g. system language, accessibility captions.

Specific selections made by the [`AVPlayerItem`](../avplayeritem.md) instance using the method [`select(_:in:)`](../avplayeritem/select%28_,in%29.md) method within any group will override automatic selection in that group until the player item receives a [`selectMediaOptionAutomatically(in:)`](../avplayeritem/selectmediaoptionautomatically%28in%29.md) message.

## Parameters

- `criteria`: An instance of [`AVPlayerMediaSelectionCriteria`](../avplayermediaselectioncriteria.md) that specifies the selection criteria.
- `mediaCharacteristic`: The media characteristic for which the selection criteria are to be applied. Supported values include [`audible`](../avmediacharacteristic/audible.md), [`legible`](../avmediacharacteristic/legible.md), and [`visual`](../avmediacharacteristic/visual.md). See Media Characteristics in the `AVFoundation Constants`.

## See Also

### Configuring media selection criteria
- [var appliesMediaSelectionCriteriaAutomatically: Bool](./appliesmediaselectioncriteriaautomatically.md)
  A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.
- [func mediaSelectionCriteria(forMediaCharacteristic: AVMediaCharacteristic) -> AVPlayerMediaSelectionCriteria?](./mediaselectioncriteria%28formediacharacteristic%29.md)
  Returns the automatic selection criteria for media items with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/setmediaselectioncriteria(_:formediacharacteristic:))*