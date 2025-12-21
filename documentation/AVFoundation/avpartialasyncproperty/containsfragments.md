# containsFragments

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether at least one movie fragment extends the asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var containsFragments: AVAsyncProperty<Root, Bool> { get }
```

#### Discussion

Use the [`load(_:isolation:)`](avasynchronouskeyvalueloading/load(_:isolation:).md) method to retrieve the property value.

For QuickTime movie files and MPEG-4 files, the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if [`canContainFragments`](avasset/cancontainfragments.md) is [`true`](https://developer.apple.com/documentation/Swift/true) and at least one `moof` box is present after the `moov` box.

## See Also

- [static var canContainFragments: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [static var overallDurationHint: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/overalldurationhint.md)
  A hint to the total duration of fragments that currently exist or may exist in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/containsfragments)*