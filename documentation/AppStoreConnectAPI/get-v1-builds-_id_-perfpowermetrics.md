# Get power and performance metrics for a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the performance and power metrics data for a specific build.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 1.4 release notes](./app-store-connect-api-1-4-release-notes.md)

#### Discussion

The example below requests iOS animation metrics on all iPads for a specific build. To get the metrics for all of the most-recent app versions instead, use the [`Get power and performance metrics for an app`](./get-v1-apps-_id_-perfpowermetrics.md) endpoint.

##### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/builds/43d3a970-273c-4bc9-88ee-aa5c05610ac1/perfPowerMetrics?filter[deviceType]=all_ipads&filter[metricType]=ANIMATION&filter[platform]=iOS
```

**Response**:

```json
{
  "productData": [
    {
      "platform": "iOS",
      "metricCategories": [
        {
          "identifier": "ANIMATION",
          "metrics": [
            {
              "identifier": "scrollHitchRate",
              "unit": {
                "identifier": "scrollHitchRate",
                "displayName": "%"
              },
              "datasets": [
                {
                  "filterCriteria": {
                    "percentile": "percentile.fifty",
                    "device": "all_ipads",
                    "deviceMarketingName": "All iPads"
                  },
                  "points": [
                    {
                      "version": "10.0",
                      "value": 6.5,
                      "goal": "fair"
                    }
                  ]
                },
                {
                  "filterCriteria": {
                    "percentile": "percentile.ninety",
                    "device": "all_ipads",
                    "deviceMarketingName": "All iPads"
                  },
                  "points": [
                    {
                      "version": "10.0",
                      "value": 29.7,
                      "goal": "poor"
                    }
                  ]
                }
              ],
              "goalKeys": [
                {
                  "goalKey": "poor",
                  "lowerBound": 10
                },
                {
                  "upperBound": 10,
                  "goalKey": "fair",
                  "lowerBound": 5
                },
                {
                  "upperBound": 5,
                  "goalKey": "good",
                  "lowerBound": 0
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "version": "1.0.0"
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/perfPowerMetrics`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The resource ID that uniquely identifies the build to return metrics data for. Obtain the build resource ID from the [`List builds`](./get-v1-builds.md) response.

### Query Parameters

- `filter[deviceType]` ([string]): Device types by which to filter. Use `all_iphones` for all iPhone models. Use `all_ipads` for all iPad models.
- `filter[metricType]` ([string]): Types of metrics by which to filter. For more information about metric types, see [`MetricCategory`](./metriccategory.md).

  **Allowed Values**: `DISK`, `HANG`, `BATTERY`, `LAUNCH`, `MEMORY`, `ANIMATION`, `TERMINATION`, `STORAGE`
- `filter[platform]` ([string]): Platforms by which to filter.

  **Allowed Values**: `IOS`

## Responses

- `200` OK (`xcodeMetrics`, `application/vnd.apple.xcode-metrics+json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Metrics and Diagnostic Logs
- [Retrieve Power and Performance Metrics and Log Insights](./retrieve-power-and-performance-metrics-and-log-insights.md)
  Use the App Store Connect API to collect and parse diagnostic logs and metrics for your apps.
- [Get power and performance metrics for an app](./get-v1-apps-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for the most recent version of an app.
- [List all diagnostic signatures for a build](./get-v1-builds-_id_-diagnosticsignatures.md)
  List the aggregate backtrace signatures captured for a specific build.
- [Download logs for a diagnostic signature](./get-v1-diagnosticsignatures-_id_-logs.md)
  Get the anonymized backtrace logs associated with a specific diagnostic signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-perfpowermetrics)*