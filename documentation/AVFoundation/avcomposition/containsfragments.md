# containsFragments

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether at least one movie fragment extends the asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var containsFragments: Bool { get }
```

#### Discussion

For QuickTime movie files and MPEG-4 files, the value is [`true`](https://developer.apple.com/documentation/Swift/true) if [`canContainFragments`](avasset/cancontainfragments.md) is [`true`](https://developer.apple.com/documentation/Swift/true) and at least one `moof` box is present after the `moov` box.

## See Also

- [var canContainFragments: Bool](avcomposition/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [var overallDurationHint: CMTime](avcomposition/overalldurationhint.md)
  The total duration of fragments that currently exist, or may exist in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/containsfragments)*