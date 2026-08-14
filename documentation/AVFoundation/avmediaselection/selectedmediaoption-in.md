# selectedMediaOption(in:)

**Framework**: AVFoundation  
**Kind**: method

Returns the media selection option that’s currently selected in the specified group.

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
func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?
```

#### Return Value

The currently selected [`AVMediaSelectionOption`](avmediaselectionoption.md). The return value may be `nil`.

#### Discussion

This method returns the currently selected [`AVMediaSelectionOption`](avmediaselectionoption.md) in the specified [`AVMediaSelectionGroup`](avmediaselectiongroup.md), but may return `nil` if media selection group’s [`allowsEmptySelection`](avmediaselectiongroup/allowsemptyselection.md) is set to [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `mediaSelectionGroup`: A media selection group obtained from the associated asset.

## See Also

- [func mediaSelectionCriteriaCanBeAppliedAutomatically(to: AVMediaSelectionGroup) -> Bool](avmediaselection/mediaselectioncriteriacanbeappliedautomatically(to:).md)
  Indicates whether the specified media selection group is subject to automatic media selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselection/selectedmediaoption(in:))*