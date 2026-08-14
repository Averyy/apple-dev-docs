# canContainFragments

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether you can extend the asset by fragments.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var canContainFragments: Bool { get }
```

#### Discussion

For QuickTime movie files and MPEG-4 files, the value is [`true`](https://developer.apple.com/documentation/swift/true) if an `mvex` box is present in the `moov` box. For those types, the `mvex` box signals the possible presence of later `moof` boxes.

## See Also

- [var containsFragments: Bool](avmutablemovie/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [var overallDurationHint: CMTime](avmutablemovie/overalldurationhint.md)
  The total duration of fragments that currently exist, or may exist in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/cancontainfragments)*