# overallDurationHint

**Framework**: AVFoundation  
**Kind**: property

A hint to the total duration of fragments that currently exist or may exist in the future.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var overallDurationHint: AVAsyncProperty<Root, CMTime> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

For QuickTime movie files and MPEG-4 files, the system obtains the value of this property from the `mehd` box of the `mvex` box, if present. If no total fragment duration hint is available, the value of this property is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid).

## See Also

- [static var canContainFragments: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [static var containsFragments: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/overalldurationhint)*