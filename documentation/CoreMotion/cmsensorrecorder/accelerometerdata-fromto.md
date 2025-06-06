# accelerometerData(from:to:)

**Framework**: Core Motion  
**Kind**: method

Retrieves the accelerometer data collected between the specified dates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func accelerometerData(from fromDate: Date, to toDate: Date) -> CMSensorDataList?
```

#### Return Value

An object to use for enumerating over the accelerometer data.

#### Discussion

Use this method to fetch accelerometer data entries in the specified date range. When fetching entries for a date range, the recorder returns only the data entries it has. If there were gaps in the recording, no data entries are returned for those gaps. Recorded accelerometer data is kept for a maximum of three days. There may be a delay of up to three minutes before new samples are available for retrieval.

## Parameters

- `fromDate`: The starting date (inclusive) from which to retrieve data. Entries occurring before this date are excluded from the results.
- `toDate`: The end date (inclusive) at which to stop retrieving data. Entries occurring after this date are excluded from the results. The difference in time between the   and this parameter must be 12 hours or less.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/accelerometerdata(from:to:))*