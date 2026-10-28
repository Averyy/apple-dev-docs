# overallDurationHint

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The total duration of fragments that currently exist, or may exist in the future.

**Availability**:
- iOS 10.2+ - Deprecated in 16.0
- iPadOS 10.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.12.2+ - Deprecated in 13.0
- tvOS 10.2+ - Deprecated in 16.0
- watchOS 3.2+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`overallDurationHint`](../avpartialasyncproperty/overalldurationhint.md) asynchronously instead.

## Declaration

```swift
var overallDurationHint: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime overallDurationHint;
```

## Discussion

For QuickTime movie files and MPEG-4 files, the asset retrieves this value from the `mehd` box of the `mvex` box, if present. If no total fragment duration hint is available, the value of this property is [`invalid`](../../CoreMedia/cmtime/invalid.md).

## See Also

### Accessing fragment support
- [canContainFragments](./cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [containsFragments](./containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/overalldurationhint)*