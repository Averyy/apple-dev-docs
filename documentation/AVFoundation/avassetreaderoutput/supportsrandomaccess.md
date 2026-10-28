# supportsRandomAccess

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetReader.outputProviderWithRandomAccess(for:) instead

## Declaration

```swift
var supportsRandomAccess: Bool { get set }
```

```objc
@property (nonatomic) BOOL supportsRandomAccess;
```

## Discussion

The default value is [`false`](../../Swift/false.md), which means you can’t reconfigure the output after reading begins. This setting may result in more efficient reading, particularly when you’re using multiple asset reader outputs.

A value of [`true`](../../Swift/true.md) indicates that you can reconfigure the output’s time ranges after reading begins by calling the [`reset(forReadingTimeRanges:)`](./reset%28forreadingtimeranges%29.md) method. This setting also prevents the asset reader from progressing to a completed state until you call the [`markConfigurationAsFinal()`](./markconfigurationasfinal%28%29.md) method.

You can’t set this value after you call [`startReading()`](../avassetreader/startreading%28%29.md) on the asset reader.

## See Also

### Configuring reading
- [var alwaysCopiesSampleData: Bool](./alwayscopiessampledata.md)
  A Boolean value that indicates whether the output vends copied sample data.
- [func reset(forReadingTimeRanges: [NSValue])](./reset%28forreadingtimeranges%29.md)
  Restarts reading with a new set of time ranges.
- [func markConfigurationAsFinal()](./markconfigurationasfinal%28%29.md)
  Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/supportsrandomaccess)*