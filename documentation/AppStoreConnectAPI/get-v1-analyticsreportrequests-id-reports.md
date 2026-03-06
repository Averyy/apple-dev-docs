# Read reports for a specific request

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of reports generated from a specific analytics report request.

**Availability**:
- App Store Connect API 3.4+

## Mentions

- [Downloading Analytics Reports](downloading-analytics-reports.md)

#### Discussion

##### Examples Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231/reports?limit=5
```

**Response**:

```json
{
  "data": [
    {
      "type": "analyticsReports",
      "id": "r19-d48c69c5-9bcb-4592-abbd-08a9411b0231",
      "attributes": {
        "name": "Streaming Playback Performance",
        "category": "PERFORMANCE"
      },
      "relationships": {
        "instances": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r19-d48c69c5-9bcb-4592-abbd-08a9411b0231/relationships/instances",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r19-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r19-d48c69c5-9bcb-4592-abbd-08a9411b0231"
      }
    },
    {
      "type": "analyticsReports",
      "id": "r20-d48c69c5-9bcb-4592-abbd-08a9411b0231",
      "attributes": {
        "name": "Streaming Downloads Performance",
        "category": "PERFORMANCE"
      },
      "relationships": {
        "instances": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r20-d48c69c5-9bcb-4592-abbd-08a9411b0231/relationships/instances",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r20-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r20-d48c69c5-9bcb-4592-abbd-08a9411b0231"
      }
    },
    {
      "type": "analyticsReports",
      "id": "r142-d48c69c5-9bcb-4592-abbd-08a9411b0231",
      "attributes": {
        "name": "App Crashes Expanded",
        "category": "PERFORMANCE"
      },
      "relationships": {
        "instances": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r142-d48c69c5-9bcb-4592-abbd-08a9411b0231/relationships/instances",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r142-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r142-d48c69c5-9bcb-4592-abbd-08a9411b0231"
      }
    },
    {
      "type": "analyticsReports",
      "id": "r143-d48c69c5-9bcb-4592-abbd-08a9411b0231",
      "attributes": {
        "name": "App Storage Reads and Writes",
        "category": "PERFORMANCE"
      },
      "relationships": {
        "instances": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r143-d48c69c5-9bcb-4592-abbd-08a9411b0231/relationships/instances",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r143-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r143-d48c69c5-9bcb-4592-abbd-08a9411b0231"
      }
    },
    {
      "type": "analyticsReports",
      "id": "r23-d48c69c5-9bcb-4592-abbd-08a9411b0231",
      "attributes": {
        "name": "AirPlay Performance",
        "category": "PERFORMANCE"
      },
      "relationships": {
        "instances": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r23-d48c69c5-9bcb-4592-abbd-08a9411b0231/relationships/instances",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r23-d48c69c5-9bcb-4592-abbd-08a9411b0231/instances"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReports/r23-d48c69c5-9bcb-4592-abbd-08a9411b0231"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231/reports?limit=5",
    "next": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231/reports?cursor=BQ.ALHoGBE&limit=5"
  },
  "meta": {
    "paging": {
      "total": 116,
      "limit": 5
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/{id}/reports`

## Parameters

- `fields[analyticsReports]` ([string])
- `filter[category]` ([string]): Possible values: - **`APP_USAGE`**: A string representing the App Usage category.
- **`APP_STORE_ENGAGEMENT`**: A string representing the App Store Engagement category.
- **`COMMERCE`**: A string representing the App Store Commerce category.
- **`FRAMEWORK_USAGE`**: A string representing the Framework Usage category.
- **`PERFORMANCE`**: A string representing the Performance category.
- `filter[name]` ([string])
- `limit` (integer)

## See Also

- [Request reports](post-v1-analyticsreportrequests.md)
  Request analytics reports for your apps.
- [Read report requests](get-v1-apps-_id_-analyticsreportrequests.md)
  Read analytics report requests for a specific app.
- [Read report request information](get-v1-analyticsreportrequests-_id_.md)
  Get details for and the state of a specific analytics report request.
- [Read reports Ids for a specific request](get-v1-analyticsreportrequests-_id_-relationships-reports.md)
  Get a list of reports Ids from a specific analytics report request.
- [Delete a report request](delete-v1-analyticsreportrequests-_id_.md)
  Remove a specific analytics report request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreportrequests-_id_-reports)*