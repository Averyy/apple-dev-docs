# selectMediaOptionAutomatically(in:)

**Framework**: AVFoundation  
**Kind**: method

Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.

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
func selectMediaOptionAutomatically(in mediaSelectionGroup: AVMediaSelectionGroup)
```

#### Discussion

This method has no effect unless the [`appliesMediaSelectionCriteriaAutomatically`](avplayer/appliesmediaselectioncriteriaautomatically.md) property of the associated [`AVPlayer`](avplayer.md) is [`true`](https://developer.apple.com/documentation/swift/true) and unless automatic media selection has previously been overridden by invoking [`select(_:in:)`](avplayeritem/select(_:in:).md).

## Parameters

- `mediaSelectionGroup`: The media selection group, obtained from the receiver’s  , that contains the specified option.

## See Also

- [var currentMediaSelection: AVMediaSelection](avplayeritem/currentmediaselection.md)
  The current media selections for each of the receiver’s media selection groups.
- [func select(AVMediaSelectionOption?, in: AVMediaSelectionGroup)](avplayeritem/select(_:in:).md)
  Selects a media option in a given media selection group and deselects all other options in that group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/selectmediaoptionautomatically(in:))*