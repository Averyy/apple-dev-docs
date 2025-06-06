# statisticsReportFrequency

**Framework**: Network Extension  
**Kind**: property

The frequencty at which to provide flow statistics to the data provider.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
var statisticsReportFrequency: NEFilterReport.Frequency { get set }
```

#### Discussion

This property determines the frequency at which the provider receives a call to its [`handle(_:)`](nefilterprovider/handle(_:).md) method with an [`NEFilterReport.Event.statistics`](nefilterreport/event-swift.enum/statistics.md) event.

The default value of this property [`NEFilterReport.Frequency.none`](nefilterreport/frequency/none.md), meaning that the provider receives no statistics by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/statisticsreportfrequency)*