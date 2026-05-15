# Read a List of a Report Instant IDs

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read list of all the instance IDs for a specific type of analytics report.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/analyticsReports/{id}/relationships/instances`

## Parameters

- `limit` (integer)

## See Also

- [Read Report Information](get-v1-analyticsreports-_id_.md)
  Get details for a specific analytics report.
- [Read a List of Instances of a Report](get-v1-analyticsreports-_id_-instances.md)
  Read list of all the granularity options for a specific type of analytics report.
- [Read Report Instance Information](get-v1-analyticsreportinstances-_id_.md)
  Get details for a specific instance of an analytics report.
- [Read the Segments for a Report](get-v1-analyticsreportinstances-_id_-segments.md)
  Get details for a specific analytics report segment.
- [Read Segment IDs for a Report](get-v1-analyticsreportinstances-_id_-relationships-segments.md)
  Get Ids for a specific analytics report segment.
- [Read the Details for a Report Segment](get-v1-analyticsreportsegments-_id_.md)
  Get details and download information for a specific analytics report segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreports-_id_-relationships-instances)*