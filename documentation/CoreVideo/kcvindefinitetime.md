# kCVIndefiniteTime

**Framework**: Core Video  
**Kind**: var  
**Role**: Global Variable

An unknown or indefinite time. For example, [`CVDisplayLinkGetNominalOutputVideoRefreshPeriod(_:)`](./cvdisplaylinkgetnominaloutputvideorefreshperiod%28_%29.md) returns `kCVIndefiniteTime` if the display link specified is not valid.

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
let kCVIndefiniteTime: CVTime
```

```c
extern const CVTime kCVIndefiniteTime;
```

## See Also

### Constants
- [let kCVZeroTime: CVTime](./kcvzerotime.md)
  Zero time or duration. For example, [`CVDisplayLinkGetOutputVideoLatency(_:)`](./cvdisplaylinkgetoutputvideolatency%28_%29.md) returns `kCVZeroTime` for zero video latency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvindefinitetime)*