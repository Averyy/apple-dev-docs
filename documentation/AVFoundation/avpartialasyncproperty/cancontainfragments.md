# canContainFragments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether you can extend the asset by fragments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var canContainFragments: AVAsyncProperty<Root, Bool> { get }
```

Available when `Root` inherits `AVAsset`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

For QuickTime movie files and MPEG-4 files, the value is [`true`](../../Swift/true.md) if an `mvex` box is present in the `moov` box. For those types, the `mvex` box signals the possible presence of later `moof` boxes.

## See Also

### Loading fragment support
- [static var containsFragments: AVAsyncProperty<Root, Bool>](./containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [static var overallDurationHint: AVAsyncProperty<Root, CMTime>](./overalldurationhint.md)
  A hint to the total duration of fragments that currently exist or may exist in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/cancontainfragments)*