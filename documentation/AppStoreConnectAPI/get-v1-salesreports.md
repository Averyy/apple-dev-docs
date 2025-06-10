# Download Sales and Trends Reports

**Framework**: App Store Connect API  
**Kind**: httpRequest

Download sales and trends reports filtered by your specified criteria.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [Downloading Analytics Reports](downloading-analytics-reports.md)
- [App Store Connect API 3.2 release notes](app-store-connect-api-3-2-release-notes.md)
- [App Store Connect API 3.4 release notes](app-store-connect-api-3-4-release-notes.md)
- [App Store Connect API 1.8 release notes](app-store-connect-api-1-8-release-notes.md)
- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)

#### Discussion

##### Allowed Values Based on Sales Report Type

Each sales report type has specific valid values for `reportType`, `reportSubType`, `frequency`, and `version`. If you use other types, it results in an error. For more details on each report type, see [`Download and view reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/view-sales-and-trends/download-and-view-reports).

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

## See Also

- [Download Finance Reports](get-v1-financereports.md)
  Download finance reports filtered by your specified criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-salesreports)*