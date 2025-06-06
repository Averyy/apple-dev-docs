# to

**Framework**: SensorKit  
**Kind**: property

Fetches sample information that occurs before this time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var to: SRAbsoluteTime { get set }
```

#### Discussion

The framework requires the app to define a value for this property. If an app fails to define this property, the framework responds to the fetch by providing [`SRError.Code.fetchRequestInvalid`](srerror/code/fetchrequestinvalid.md) to the reader delegate via [`sensorReader(_:fetching:failedWithError:)`](srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:).md).

## See Also

- [var from: SRAbsoluteTime](srfetchrequest/from.md)
  Fetches sample information that occurs after this time.
- [struct SRAbsoluteTime](srabsolutetime.md)
  A value that describes when the system records the data.
- [static func current() -> SRAbsoluteTime](srabsolutetime/current.md)
  Provides the current absolute time.
- [func toCFAbsoluteTime() -> CFAbsoluteTime](srabsolutetime/tocfabsolutetime.md)
  Converts an absolute time to a core-foundation absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to)*