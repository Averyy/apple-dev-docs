# sourceTimeRanges

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of time ranges.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sourceTimeRanges: [NSValue] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSValue *> * sourceTimeRanges;
```

#### Discussion

Each element in the array is an [`NSValue`](../../Foundation/nsvalue.md) object that wraps a [`CMTimeRange`](../../CoreMedia/cmtimerange.md) structure that represents one source time range. The value of this property is suitable to pass to the [`reset(forReadingTimeRanges:)`](../avassetreaderoutput/reset%28forreadingtimeranges%29.md) method of [`AVAssetReaderOutput`](../avassetreaderoutput.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription/sourcetimeranges)*