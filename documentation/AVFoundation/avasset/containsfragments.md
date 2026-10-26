# containsFragments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether at least one movie fragment extends the asset.

**Availability**:
- iOS 9.0+ - Deprecated in 16.0
- iPadOS 9.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0

> **Deprecated**: Load the value of [`containsFragments`](../avpartialasyncproperty/containsfragments.md) asynchronously instead.

## Declaration

```swift
var containsFragments: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL containsFragments;
```

#### Discussion

For QuickTime movie files and MPEG-4 files, the value is [`true`](../../Swift/true.md) if [`canContainFragments`](./cancontainfragments.md) is [`true`](../../Swift/true.md) and at least one `moof` box is present after the `moov` box.

## See Also

### Accessing fragment support
- [canContainFragments](./cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [overallDurationHint](./overalldurationhint.md)
  The total duration of fragments that currently exist, or may exist in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/containsfragments)*