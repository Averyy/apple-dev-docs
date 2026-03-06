# Download Finance Reports

**Framework**: App Store Connect API  
**Kind**: httpRequest

Download finance reports filtered by your specified criteria.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [Downloading Analytics Reports](downloading-analytics-reports.md)

#### Discussion

For more information see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/financeReports`

## Parameters

- `filter[regionCode]` ([string]) *(required)*: You can download consolidated or separate financial reports per territory. For a complete list of possible values, see [`Financial report regions and currencies`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/financial-report-regions-and-currencies).
- `filter[reportDate]` ([string]) *(required)*: The fiscal month of the report you wish to download based on the [`Apple Fiscal Calendar`](https://developer.apple.comhttps://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/wa/jumpTo?page=fiscalcalendar). The fiscal month is specified in the `YYYY-MM` format.
- `filter[reportType]` ([string]) *(required)*: This value is always `FINANCIAL`.
- `filter[vendorNumber]` ([string]) *(required)*: You can find your vendor number in [`View payments and proceeds`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/view-payments-and-proceeds).

## See Also

- [Download Sales and Trends Reports](get-v1-salesreports.md)
  Download sales and trends reports filtered by your specified criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-financereports)*