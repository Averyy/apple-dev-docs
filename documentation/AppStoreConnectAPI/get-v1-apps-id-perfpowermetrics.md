# Get Power and Performance Metrics for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the performance and power metrics data for the most recent version of an app.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 1.4 release notes](app-store-connect-api-1-4-release-notes.md)
- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)

#### Discussion

The example below requests iOS app launch metrics on all iPhones for the most-recent app versions. To get metrics for a specific app version instead, use the [`Get Power and Performance Metrics for a Build`](get-v1-builds-_id_-perfpowermetrics.md) endpoint.

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/161309721/perfPowerMetrics?filter[deviceType]=all_iphones&filter[metricType]=LAUNCH&filter[platform]=iOS
```

**Response**:

```json
{
  "version": "1.0.0",
  "insights": {
    "regressions": [
      {
        "latestVersion": "2.0",
        "maxLatestVersionValue": 2014.3,
        "metric": "launchTime",
        "metricCategory": "LAUNCH",
        "populations": [
          {
            "deltaPercentage": 10,
            "device": "all_iphones",
            "latestVersionValue": 997.8,
            "percentile": "percentile.fifty",
            "referenceAverageValue": 907.48,
            "summaryString": "Increased 10% across iPhone (All)"
          },
          {
            "deltaPercentage": 13,
            "device": "all_iphones",
            "latestVersionValue": 2014.3,
            "percentile": "percentile.ninety",
            "referenceAverageValue": 1777.88,
            "summaryString": "Increased 13% across iPhone (All)"
          }
        ],
        "referenceVersions": ["1.0", "1.1", "1.2", "1.3"],
        "summaryString": "Top (90th percentile) and typical (50th percentile) Launch Time trended up between app versions 1.0 to 2.0 on iPhone (All). The maximum value for the latest app version is at 2014.30 ms and increased between 10% to 13% compared to the average for previous 4 app versions."
      }
    ],
    "trendingUp": []
  },
  "productData": [
    {
      "platform": "iOS",
      "metricCategories": [
        {
          "identifier": "LAUNCH",
          "metrics": [
            {
              "identifier": "launchTime",
              "unit": {
                "displayName": "ms",
                "identifier": "milliseconds"
              },
              "datasets": [
                {
                  "filterCriteria": {
                    "device": "all_iphones",
                    "deviceMarketingName": "All iPhones",
                    "percentile": "percentile.fifty"
                  },
                  "points": [
                    {
                      "value": 768.7,
                      "version": "1.0"
                    },
                    {
                      "value": 750,
                      "version": "1.1"
                    },
                    {
                      "value": 992.3,
                      "version": "1.2"
                    },
                    {
                      "value": 1118.9,
                      "version": "1.3"
                    },
                    {
                      "value": 997.8,
                      "version": "2.0"
                    }
                  ]
                },
                {
                  "filterCriteria": {
                    "device": "all_iphones",
                    "deviceMarketingName": "All iPhones",
                    "percentile": "percentile.ninety"
                  },
                  "points": [
                    {
                      "value": 1532.1,
                      "version": "1.0"
                    },
                    {
                      "value": 1390.2,
                      "version": "1.1"
                    },
                    {
                      "value": 2030.8,
                      "version": "1.2"
                    },
                    {
                      "value": 2158.4,
                      "version": "1.3"
                    },
                    {
                      "value": 2014.3,
                      "version": "2.0"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/perfPowerMetrics`

## Parameters

- `filter[deviceType]` ([string]): The device types by which to filter. Use `all_iphones` for all iPhone models. Use `all_ipads` for all iPad models.
- `filter[metricType]` ([string]): Types of metrics by which to filter. For more information about metric types, see [`MetricCategory`](metriccategory.md).
- `filter[platform]` ([string]): Platforms by which to filter.

## See Also

- [Retrieve Power and Performance Metrics and Log Insights](retrieve-power-and-performance-metrics-and-log-insights.md)
  Use the App Store Connect API to collect and parse diagnostic logs and metrics for your apps.
- [Get Power and Performance Metrics for a Build](get-v1-builds-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for a specific build.
- [List All Diagnostic Signatures for a Build](get-v1-builds-_id_-diagnosticsignatures.md)
  List the aggregate backtrace signatures captured for a specific build.
- [Download Logs for a Diagnostic Signature](get-v1-diagnosticsignatures-_id_-logs.md)
  Get the anonymized backtrace logs associated with a specific diagnostic signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-perfpowermetrics)*