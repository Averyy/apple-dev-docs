# containsFragments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether at least one movie fragment extends the asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var containsFragments: AVAsyncProperty<Root, Bool> { get }
```

Available when `Root` inherits `AVAsset`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

For QuickTime movie files and MPEG-4 files, the value of this property is [`true`](../../Swift/true.md) if [`canContainFragments`](../avasset/cancontainfragments.md) is [`true`](../../Swift/true.md) and at least one `moof` box is present after the `moov` box.

## See Also

### Loading fragment support
- [static var canContainFragments: AVAsyncProperty<Root, Bool>](./cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [static var overallDurationHint: AVAsyncProperty<Root, CMTime>](./overalldurationhint.md)
  A hint to the total duration of fragments that currently exist or may exist in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/containsfragments)*