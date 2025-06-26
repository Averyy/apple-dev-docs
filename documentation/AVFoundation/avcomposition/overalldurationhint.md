# overallDurationHint

**Framework**: AVFoundation  
**Kind**: property

The total duration of fragments that currently exist, or may exist in the future.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var overallDurationHint: CMTime { get }
```

#### Discussion

For QuickTime movie files and MPEG-4 files, the asset retrieves this value from the `mehd` box of the `mvex` box, if present. If no total fragment duration hint is available, the value of this property is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid).

## See Also

- [var canContainFragments: Bool](avcomposition/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [var containsFragments: Bool](avcomposition/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/overalldurationhint)*