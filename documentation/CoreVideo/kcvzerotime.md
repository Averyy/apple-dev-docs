# kCVZeroTime

**Framework**: Core Video  
**Kind**: var

Zero time or duration. For example, [`CVDisplayLinkGetOutputVideoLatency(_:)`](cvdisplaylinkgetoutputvideolatency(_:).md) returns `kCVZeroTime` for zero video latency.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let kCVZeroTime: CVTime
```

## See Also

- [let kCVIndefiniteTime: CVTime](kcvindefinitetime.md)
  An unknown or indefinite time. For example, [`CVDisplayLinkGetNominalOutputVideoRefreshPeriod(_:)`](cvdisplaylinkgetnominaloutputvideorefreshperiod(_:).md) returns `kCVIndefiniteTime` if the display link specified is not valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvzerotime)*