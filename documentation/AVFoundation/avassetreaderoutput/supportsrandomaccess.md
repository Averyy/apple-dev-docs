# supportsRandomAccess

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var supportsRandomAccess: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false), which means you can’t reconfigure the output after reading begins. This setting may result in more efficient reading, particularly when you’re using multiple asset reader outputs.

A value of [`true`](https://developer.apple.com/documentation/swift/true) indicates that you can reconfigure the output’s time ranges after reading begins by calling the [`reset(forReadingTimeRanges:)`](avassetreaderoutput/reset(forreadingtimeranges:).md) method. This setting also prevents the asset reader from progressing to a completed state until you call the [`markConfigurationAsFinal()`](avassetreaderoutput/markconfigurationasfinal().md) method.

You can’t set this value after you call [`startReading()`](avassetreader/startreading().md) on the asset reader.

## See Also

- [var alwaysCopiesSampleData: Bool](avassetreaderoutput/alwayscopiessampledata.md)
  A Boolean value that indicates whether the output vends copied sample data.
- [func reset(forReadingTimeRanges: [NSValue])](avassetreaderoutput/reset(forreadingtimeranges:).md)
  Restarts reading with a new set of time ranges.
- [func markConfigurationAsFinal()](avassetreaderoutput/markconfigurationasfinal.md)
  Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/supportsrandomaccess)*