# markConfigurationAsFinal()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use RandomAccessController.markConfigurationAsFinal() instead

## Declaration

```swift
func markConfigurationAsFinal()
```

```objc
- (void) markConfigurationAsFinal;
```

## Discussion

When the value of the [`supportsRandomAccess`](./supportsrandomaccess.md) property is [`true`](../../Swift/true.md), the asset reader doesn’t advance to an [`AVAssetReader.Status.completed`](../avassetreader/status-swift.enum/completed.md) state until you call this method.

After you call this method, you can’t make further calls to the [`reset(forReadingTimeRanges:)`](./reset%28forreadingtimeranges%29.md) method.

When the destination of the output’s media data is an [`AVAssetWriterInput`](../avassetwriterinput.md) that you configure for multi-pass encoding, an appropriate time to call this method is after the asset writer input indicates that it doesn’t require performing additional passes.

## See Also

### Configuring reading
- [var alwaysCopiesSampleData: Bool](./alwayscopiessampledata.md)
  A Boolean value that indicates whether the output vends copied sample data.
- [var supportsRandomAccess: Bool](./supportsrandomaccess.md)
  A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads.
- [func reset(forReadingTimeRanges: [NSValue])](./reset%28forreadingtimeranges%29.md)
  Restarts reading with a new set of time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/markconfigurationasfinal())*