# canContainFragments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can extend the asset by fragments.

**Availability**:
- iOS 9.0+ - Deprecated in 16.0
- iPadOS 9.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0

> **Deprecated**: Load the value of [`canContainFragments`](../avpartialasyncproperty/cancontainfragments.md) asynchronously instead.

## Declaration

```swift
var canContainFragments: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canContainFragments;
```

#### Discussion

For QuickTime movie files and MPEG-4 files, the value is [`true`](../../Swift/true.md) if an `mvex` box is present in the `moov` box. For those types, the `mvex` box signals the possible presence of later `moof` boxes.

## See Also

### Accessing fragment support
- [containsFragments](./containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [overallDurationHint](./overalldurationhint.md)
  The total duration of fragments that currently exist, or may exist in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/cancontainfragments)*