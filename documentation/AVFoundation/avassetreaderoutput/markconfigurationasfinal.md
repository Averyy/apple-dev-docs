# markConfigurationAsFinal()

**Framework**: AVFoundation  
**Kind**: method

Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func markConfigurationAsFinal()
```

#### Discussion

When the value of the [`supportsRandomAccess`](avassetreaderoutput/supportsrandomaccess.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), the asset reader doesn’t advance to an [`AVAssetReader.Status.completed`](avassetreader/status-swift.enum/completed.md) state until you call this method.

After you call this method, you can’t make further calls to the [`reset(forReadingTimeRanges:)`](avassetreaderoutput/reset(forreadingtimeranges:).md) method.

When the destination of the output’s media data is an [`AVAssetWriterInput`](avassetwriterinput.md) that you configure for multi-pass encoding, an appropriate time to call this method is after the asset writer input indicates that it doesn’t require performing additional passes.

## See Also

- [var alwaysCopiesSampleData: Bool](avassetreaderoutput/alwayscopiessampledata.md)
  A Boolean value that indicates whether the output vends copied sample data.
- [var supportsRandomAccess: Bool](avassetreaderoutput/supportsrandomaccess.md)
  A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads.
- [func reset(forReadingTimeRanges: [NSValue])](avassetreaderoutput/reset(forreadingtimeranges:).md)
  Restarts reading with a new set of time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/markconfigurationasfinal())*