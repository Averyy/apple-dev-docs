# Read report instance information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details for a specific instance of an analytics report.

**Availability**:
- App Store Connect API 3.4+

#### Discussion

> **Note**:  If you don’t retrieve data for a long time, a report request changes to `stoppedDueToInactivity`. You need to make a new request to resume getting reports.

##### Examples Request and Response

## See Also

- [Read report information](get-v1-analyticsreports-_id_.md)
  Get details for a specific analytics report.
- [Read a list of instances of a report](get-v1-analyticsreports-_id_-instances.md)
  Read list of all the granularity options for a specific type of analytics report.
- [Read the segments for a report](get-v1-analyticsreportinstances-_id_-segments.md)
  Get details for a specific analytics report segment.
- [Read segment IDs for a report](get-v1-analyticsreportinstances-_id_-relationships-segments.md)
  Get Ids for a specific analytics report segment.
- [Read the details for a report segment](get-v1-analyticsreportsegments-_id_.md)
  Get details and download information for a specific analytics report segment.
- [Read a list of a report instant IDs](get-v1-analyticsreports-_id_-relationships-instances.md)
  Read list of all the instance IDs for a specific type of analytics report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreportinstances-_id_)*