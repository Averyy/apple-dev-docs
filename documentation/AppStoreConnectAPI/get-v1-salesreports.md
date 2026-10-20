# Download sales and trends reports

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Download sales and trends reports filtered by your specified criteria.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [App Store Connect API 1.8 release notes](./app-store-connect-api-1-8-release-notes.md)
- [App Store Connect API 3.2 release notes](./app-store-connect-api-3-2-release-notes.md)
- [App Store Connect API 3.4 release notes](./app-store-connect-api-3-4-release-notes.md)
- [App Store Connect API 3.6 release notes](./app-store-connect-api-3-6-release-notes.md)
- [App Store Connect API 3.7 release notes](./app-store-connect-api-3-7-release-notes.md)
- [Downloading Analytics Reports](./downloading-analytics-reports.md)

#### Discussion

##### Allowed values based on sales report type

Each sales report type has specific valid values for `reportType`, `reportSubType`, `frequency`, and `version`. If you use other types, it results in an error. For more details on each report type, see [Download and view reports](https://developer.apple.com/help/app-store-connect/view-sales-and-trends/download-and-view-reports).

> **Note**:  Version 1_2 of the Subscription, Subscription Event, and Subscriber reports in Sales and Trends is no longer available for download.

| `reportType` | `reportSubType` | `frequency` | `version` |
| --- | --- | --- | --- |
| FIRST_ANNUAL | DETAILED | DAILY | 1_0 |
| FIRST_ANNUAL | SUMMARY | YEARLY | 1_0 |
| INSTALLS | SUMMARY_CHANNEL | YEARLY | 1_0, 1_1 |
| INSTALLS | SUMMARY_INSTALL_TYPE | YEARLY | 1_0, 1_1 |
| INSTALLS | SUMMARY | MONTHLY | 1_2 |
| INSTALLS | SUMMARY_TERRITORY | YEARLY | 1_0, 1_1 |
| INSTALLS | DETAILED | MONTHLY | 1_2 |
| INSTALLS | DETAILED | YEARLY | 1_0, 1_1 |
| NEWSSTAND | DETAILED | DAILY, WEEKLY | 1_0 |
| PRE_ORDER | SUMMARY | DAILY, WEEKLY, MONTHLY, YEARLY | 1_0 |
| SALES | SUMMARY | DAILY, WEEKLY, MONTHLY, YEARLY | 1_0 |
| SUBSCRIBER | DETAILED | DAILY | 1_3 |
| SUBSCRIPTION | SUMMARY | DAILY | 1_3 |
| SUBSCRIPTION_EVENT | SUMMARY | DAILY | 1_3 |
| SUBSCRIPTION_OFFER_CODE_REDEMPTION | SUMMARY | DAILY | 1_0 |
| WIN_BACK_ELIGIBILITY | SUMMARY | DAILY | 1_0 |

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/salesReports`

## Parameters

### Query Parameters

- `filter[frequency]` ([string]) *(required)*: Frequency of the report to download. For a list of values, see Allowed values based on sales report type table below.

  **Allowed Values**: `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`
- `filter[reportDate]` ([string]): The report date to download. Specify the date in the `YYYY-MM-DD` format for all report frequencies except `DAILY`, which doesn’t require a date. For more information, see [report availability and storage](https://help.apple.com/itc/appssalesandtrends/#/itc48f999955).
- `filter[reportSubType]` ([string]) *(required)*: The report sub type to download. For a list of values, see Allowed values based on sales report type table below.

  **Allowed Values**: `SUMMARY`, `DETAILED`, `SUMMARY_INSTALL_TYPE`, `SUMMARY_TERRITORY`, `SUMMARY_CHANNEL`
- `filter[reportType]` ([string]) *(required)*: The report to download. For more details on each report type see [Download and view reports](https://help.apple.com/itc/appssalesandtrends/#/itc37a18bcbf).

  **Allowed Values**: `SALES`, `PRE_ORDER`, `NEWSSTAND`, `SUBSCRIPTION`, `SUBSCRIPTION_EVENT`, `SUBSCRIBER`, `SUBSCRIPTION_OFFER_CODE_REDEMPTION`, `INSTALLS`, `FIRST_ANNUAL`, `WIN_BACK_ELIGIBILITY`
- `filter[vendorNumber]` ([string]) *(required)*: You can find your vendor number in [View payments and proceeds](https://developer.apple.com/help/app-store-connect/getting-paid/view-payments-and-proceeds).
- `filter[version]` ([string]): The version of the report. For a list of values, see Allowed values based on sales report type table below.

## Responses

- `200` OK (`gzip`, `application/a-gzip`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Downloading Reports
- [Download finance reports](./get-v1-financereports.md)
  Download finance reports filtered by your specified criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-salesreports)*