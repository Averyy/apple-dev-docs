# setMediaSelectionCriteria(_:forMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

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

#### Discussion

Criteria will be applied to an [`AVPlayerItem`](avplayeritem.md) instance when:

- It is made ready to play.
- Specific media selections are made by the [`AVPlayerItem`](avplayeritem.md) instance using the method [`select(_:in:)`](avplayeritem/select(_:in:).md) in a different group. The automatic choice in one group may be influenced by a specific selection in another group.
- Underlying system preferences change, e.g. system language, accessibility captions.

Specific selections made by the [`AVPlayerItem`](avplayeritem.md) instance using the method [`select(_:in:)`](avplayeritem/select(_:in:).md) method within any group will override automatic selection in that group until the player item receives a [`selectMediaOptionAutomatically(in:)`](avplayeritem/selectmediaoptionautomatically(in:).md) message.

## Parameters

- `criteria`: An instance of   that specifies the selection criteria.
- `mediaCharacteristic`: The media characteristic for which the selection criteria are to be applied. Supported values include  ,  , and  . See Media Characteristics in the  .

## See Also

- [var appliesMediaSelectionCriteriaAutomatically: Bool](avplayer/appliesmediaselectioncriteriaautomatically.md)
  A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.
- [func mediaSelectionCriteria(forMediaCharacteristic: AVMediaCharacteristic) -> AVPlayerMediaSelectionCriteria?](avplayer/mediaselectioncriteria(formediacharacteristic:).md)
  Returns the automatic selection criteria for media items with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/setmediaselectioncriteria(_:formediacharacteristic:))*