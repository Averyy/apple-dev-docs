# Read report information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details for a specific analytics report.

**Availability**:
- App Store Connect API 3.4+

#### Discussion

##### Examples Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/analyticsReports/r2-d48c69c5-9bcb-4592-abbd-08a9411b0231
```

**Response**:

```json
{
  "data": {
    "type": "analyticsReports",
    "id": "r2-d48c69c5-9bcb-4592-abbd-08a9411b0231",
    "attributes": {
      "name": "App Crashes",
      "category": "APP_USAGE"
    },
    "relationships": {
      "instances": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r2-d48c69c5-9bcb-4592-abbd-08a9411b0231/relationships/instances",
          "related": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r2-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r2-d48c69c5-9bcb-4592-abbd-08a9411b0231"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r2-d48c69c5-9bcb-4592-abbd-08a9411b0231"
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/analyticsReports/{id}`

## Parameters

- `fields[analyticsReports]` ([string])

## See Also

- [Read a list of instances of a report](get-v1-analyticsreports-_id_-instances.md)
  Read list of all the granularity options for a specific type of analytics report.
- [Read report instance information](get-v1-analyticsreportinstances-_id_.md)
  Get details for a specific instance of an analytics report.
- [Read the segments for a report](get-v1-analyticsreportinstances-_id_-segments.md)
  Get details for a specific analytics report segment.
- [Read segment IDs for a report](get-v1-analyticsreportinstances-_id_-relationships-segments.md)
  Get Ids for a specific analytics report segment.
- [Read the details for a report segment](get-v1-analyticsreportsegments-_id_.md)
  Get details and download information for a specific analytics report segment.
- [Read a list of a report instant IDs](get-v1-analyticsreports-_id_-relationships-instances.md)
  Read list of all the instance IDs for a specific type of analytics report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreports-_id_)*