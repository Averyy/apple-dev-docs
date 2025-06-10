# init(videoTime:hostTime:rateScaler:videoRefreshPeriod:smpteTime:topField:bottomField:)

**Framework**: Core Video  
**Kind**: init

Initialize a CVTimeStamp containing specified fields. The bits corrsrponding to non-nil arguments are set in `CVTimeStamp.flags`.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@backDeployed(before: macOS 16.0, iOS 19.0, tvOS 19.0, watchOS 12.0, visionOS 3.0)
init(videoTime: CVTime? = nil, hostTime: UInt64? = nil, rateScaler: Double? = nil, videoRefreshPeriod: Int64? = nil, smpteTime: CVSMPTETime? = nil, topField: Bool = false, bottomField: Bool = false)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtimestamp/init(videotime:hosttime:ratescaler:videorefreshperiod:smptetime:topfield:bottomfield:))*