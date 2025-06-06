# mediaSelectionCriteriaCanBeAppliedAutomatically(to:)

**Framework**: AVFoundation  
**Kind**: method

Indicates whether the specified media selection group is subject to automatic media selection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func mediaSelectionCriteriaCanBeAppliedAutomatically(to mediaSelectionGroup: AVMediaSelectionGroup) -> Bool
```

#### Return Value

A Boolean value indicating whether the group is subject to automatic media selection.

#### Discussion

The automatic application of media selection criteria is suspended in any group in which a specific selection has been made by calling [`select(_:in:)`](avplayeritem/select(_:in:).md) on the current [`AVPlayerItem`](avplayeritem.md).

## Parameters

- `mediaSelectionGroup`: A media selection group obtained from the associated asset.

## See Also

- [func selectedMediaOption(in: AVMediaSelectionGroup) -> AVMediaSelectionOption?](avmediaselection/selectedmediaoption(in:).md)
  Returns the media selection option that’s currently selected in the specified group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselection/mediaselectioncriteriacanbeappliedautomatically(to:))*