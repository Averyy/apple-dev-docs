# Read a List of Instances of a Report

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read list of all the granularity options for a specific type of analytics report.

**Availability**:
- App Store Connect API 3.4+

## Mentions

- [Downloading Analytics Reports](downloading-analytics-reports.md)

#### Discussion

##### Examples Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/analyticsReports/r2-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances?limit=3&filter%5Bgranularity%5D=DAILY
```

**Response**:

```json
{
  "data": [
    {
      "type": "analyticsReportInstances",
      "id": "5c43f2fa-aae7-4290-8664-d6551784c508",
      "attributes": {
        "granularity": "DAILY",
        "processingDate": "2024-01-23"
      },
      "relationships": {
        "segments": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/5c43f2fa-aae7-4290-8664-d6551784c508/relationships/segments",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/5c43f2fa-aae7-4290-8664-d6551784c508/segments"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/5c43f2fa-aae7-4290-8664-d6551784c508"
      }
    },
    {
      "type": "analyticsReportInstances",
      "id": "42b3c667-3d79-47d0-8ee9-775f685a777c",
      "attributes": {
        "granularity": "DAILY",
        "processingDate": "2024-01-24"
      },
      "relationships": {
        "segments": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/42b3c667-3d79-47d0-8ee9-775f685a777c/relationships/segments",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/42b3c667-3d79-47d0-8ee9-775f685a777c/segments"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/42b3c667-3d79-47d0-8ee9-775f685a777c"
      }
    },
    {
      "type": "analyticsReportInstances",
      "id": "d4a141c8-7647-4bdf-b9ae-04cab705d641",
      "attributes": {
        "granularity": "DAILY",
        "processingDate": "2024-01-25"
      },
      "relationships": {
        "segments": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/d4a141c8-7647-4bdf-b9ae-04cab705d641/relationships/segments",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/d4a141c8-7647-4bdf-b9ae-04cab705d641/segments"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportInstances/d4a141c8-7647-4bdf-b9ae-04cab705d641"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r2-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances?limit=3&filter%5Bgranularity%5D=DAILY",
    "next": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r2-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances?cursor=Aw.VGkW1w&limit=3&filter%5Bgranularity%5D=DAILY"
  },
  "meta": {
    "paging": {
      "total": 6,
      "limit": 3
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/analyticsReports/{id}/instances`

## Parameters

- `fields[analyticsReportInstances]` ([string])
- `filter[granularity]` ([string])
- `filter[processingDate]` ([string]): Use ISO 8601 YYYY-MM-DD.
- `limit` (integer)

## See Also

- [Read Report Information](get-v1-analyticsreports-_id_.md)
  Get details for a specific analytics report.
- [Read Report Instance Information](get-v1-analyticsreportinstances-_id_.md)
  Get details for a specific instance of an analytics report.
- [Read the Segments for a Report](get-v1-analyticsreportinstances-_id_-segments.md)
  Get details for a specific analytics report segment.
- [Read Segment IDs for a Report](get-v1-analyticsreportinstances-_id_-relationships-segments.md)
  Get Ids for a specific analytics report segment.
- [Read the Details for a Report Segment](get-v1-analyticsreportsegments-_id_.md)
  Get details and download information for a specific analytics report segment.
- [Read a List of a Report Instant IDs](get-v1-analyticsreports-_id_-relationships-instances.md)
  Read list of all the instance IDs for a specific type of analytics report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreports-_id_-instances)*