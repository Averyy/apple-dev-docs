# alwaysCopiesSampleData

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the output vends copied sample data.

**Availability**:
- iOS 5.0+ - Deprecated in 27.0
- iPadOS 5.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: It is not necessary to copy the sample data in order to make it safe to use the vended buffer

## Declaration

```swift
var alwaysCopiesSampleData: Bool { get set }
```

```objc
@property (nonatomic) BOOL alwaysCopiesSampleData;
```

## Discussion

The default value is [`true`](../../Swift/true.md), which indicates that the output always provides copies of sample data to your app. This is the appropriate property value if you intend to modify the sample data it returns.

You can disable the default behavior by setting the value to [`false`](../../Swift/false.md), which causes the output to vend buffers that may not be copies. Your app can reference these buffers, but it can’t modify them because the result of modifying a shared buffer isn’t defined. If you don’t need to modify the sample data, disabling copying may lead to performance improvements.

## See Also

### Configuring reading
- [var supportsRandomAccess: Bool](./supportsrandomaccess.md)
  A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads.
- [func reset(forReadingTimeRanges: [NSValue])](./reset%28forreadingtimeranges%29.md)
  Restarts reading with a new set of time ranges.
- [func markConfigurationAsFinal()](./markconfigurationasfinal%28%29.md)
  Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/alwayscopiessampledata)*