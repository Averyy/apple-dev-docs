# statisticsReportFrequency

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The frequency at which the data provider receives reports.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
var statisticsReportFrequency: NEFilterReport.Frequency { get set }
```

```objc
@property NEFilterReportFrequency statisticsReportFrequency;
```

#### Discussion

This property determines the frequency at which the system calls the data provider’s [`handle(_:)`](../nefilterprovider/handle%28_%29.md) method with an [`NEFilterReport`](../nefilterreport.md) instance that contains an [`NEFilterReport.Event.statistics`](../nefilterreport/event-swift.enum/statistics.md) [`event`](../nefilterreport/event-swift.property.md).

## See Also

### Inspecting new flow verdict properties
- [NEFilterReport.Frequency](../nefilterreport/frequency.md)
  An enumeration that represents the frequency of filter report delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/statisticsreportfrequency)*