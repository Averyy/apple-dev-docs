# from

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

Fetches sample information that occurs after this time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var from: SRAbsoluteTime { get set }
```

```objc
@property (assign) SRAbsoluteTime from;
```

#### Discussion

A fetch is exclusive of this time.

The framework requires the app to define a value for this property. If an app fails to define this property, the framework responds to the fetch by providing [`SRError.Code.fetchRequestInvalid`](../srerror/code/fetchrequestinvalid.md) to the reader delegate via [`sensorReader(_:fetching:failedWithError:)`](../srsensorreaderdelegate/sensorreader%28_,fetching,failedwitherror%29.md).

## See Also

### Defining the Time Range
- [var to: SRAbsoluteTime](./to.md)
  Fetches sample information that occurs before this time.
- [struct SRAbsoluteTime](../srabsolutetime.md)
  A value that describes when the system records the data.
- [static func current() -> SRAbsoluteTime](../srabsolutetime/current%28%29.md)
  Provides the current absolute time.
- [func toCFAbsoluteTime() -> CFAbsoluteTime](../srabsolutetime/tocfabsolutetime%28%29.md)
  Converts an absolute time to a core-foundation absolute time.
- [SRAbsoluteTimeFromCFAbsoluteTime](../srabsolutetimefromcfabsolutetime.md)
  Provides an absolute time equivalent to the argument core-foundation absolute time.
- [SRAbsoluteTimeFromContinuousTime](../srabsolutetimefromcontinuoustime.md)
  Provides an absolute time equivalent to the argument continuous time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchrequest/from)*