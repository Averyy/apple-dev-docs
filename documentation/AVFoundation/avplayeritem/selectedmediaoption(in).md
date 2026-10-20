# selectedMediaOption(in:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the media selection option that’s currently selected from the specified group.

**Availability**:
- iOS 5.0+ - Deprecated in 11.0
- iPadOS 5.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`currentMediaSelection`](./currentmediaselection.md) instead.

## Declaration

```swift
func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?
```

```objc
- (AVMediaSelectionOption *) selectedMediaOptionInMediaSelectionGroup:(AVMediaSelectionGroup *) mediaSelectionGroup;
```

#### Return Value

An instance of [`AVMediaSelectionOption`](../avmediaselectionoption.md) that describes the currently selected option in the group.

#### Discussion

If the value of the [`allowsEmptySelection`](../avmediaselectiongroup/allowsemptyselection.md) property of `mediaSelectionGroup` is [`true`](../../Swift/true.md), the currently selected option in the group may be `nil`.

## Parameters

- `mediaSelectionGroup`: A media selection group obtained from the player item’s asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/selectedmediaoption(in:))*