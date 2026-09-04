# attributionToken()

**Framework**: AdServices  
**Kind**: method

Generates a token.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 11.1+
- visionOS 1.0+

## Declaration

```swift
class func attributionToken() throws -> String
```

#### Discussion

The token that the framework returns is a Base64 encoded string and has a 24-hour TTL. You can provide the token to a Mobile Measurement Provider (MMP), or app developers can use it to make a `POST` API call to fetch attribution records within the 24-hour TTL window. Use a single token in the request body and use a content-type of `text/plain` in the header, as the following example shows:

```other
POST https://api-adservices.apple.com/api/v1/
--header 'Content-Type: text/plain' \
--data-raw

G9i5hC8lQJeGOfmS+MFycll/025oJEjtpZ+rs4AUkDEJh52fT8RrjwIR/h+2JOpXz4MRdmtcemL8WTTHfNN52tjqjbWupke40AAAAVADAAAAvQAAAIAgQF1+XF4Tl2IZ7Bw/M6ufUHt+UcIhuBeJT8YenB2v36bnZKEjvq/IH8rqXkRELTHdyiqOYtpy837+UjF/NjE6t1/l7sIn71b0t3FEXJd8QOtl3Bi6iQyJgGeN8w8X0MK1PDqz9nLJtRD/wl+p112qR2YrMDyyKnwNrbfRhnGB9AAAAB7wAXlwNHelWf5RT2bzSJcGflqELMCGoDEHIl7jF6kAAACfAb9ylY8ffdbTlyJODQYQ/6V9qbaBAAAAhgUBW39MQI1A0SZgNmZFz4KPaF94BxBzd4rDkjr/eSeuaXWCmEW3ZhBzE/MOM17hAPBVlDhTPcZ/2ybr3WYIkfb+AAg/7jxGpDXgTtco3fzTytnZpEaI5SenXHALIexQAUTBsfBW2HCMQuTRo+7anoWkf69656ZAWcSc3DEQ1CAkUSKO9X7iAAABBEQQBQA=
```

> ❗ **Important**: A 404 response can occur if you make an API call too quickly after receiving a valid token. A best practice is to initiate retries at intervals of 5 seconds, with a maximum of three attempts.

For details about error codes, see [`AAAttributionError`](aaattributionerror.md).

#### Response Codes

| **Response** | **Description** |
| --- | --- |
| 200 | Success. If the API finds a matching attribution record, the payload returns `attribution=true`. ![None](/images/com.apple.AdServices/spacer.png)If the API doesn’t find a matching attribution record, the payload returns `attribution=false`. In this case, the `200` `OK` response is acknowledgment of the receipt of the data request. |
| 400 | The token is invalid. |
| 404 | Not found. The API is unable to retrieve the requested attribution record.  ![None](/images/com.apple.AdServices/spacer.png)Tokens have a TTL of 24 hours. If the `POST` API call exceeds 24 hours, a `404` response returns. If your token is valid, a best practice is to initiate retries at intervals of 5 seconds with a maximum of three attempts. |
| 500 | The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later. |

#### Attribution Payloads

The attribution record is a data dictionary with key-value pairs that correspond to your Apple Ads campaigns and app downloads from devices running iOS 14 and later. Run reports to review detailed campaign metadata in the [`Apple Ads Platform API`](https://developer.apple.com/documentation/apple-ads-platform-api) or [`Apple Ads Advanced`](https://developer.apple.comhttps://ads.apple.com/advanced/).

> **Note**: If you receive test data in your payload responses, check to make sure your app isn’t in developer mode. AdServices will return a test payload when developer mode is on:

```json
{
  "attribution": true,
  "orgId": 1234567890,
  "campaignId": 1234567890,
  "conversionType": "Download",
  "clickDate": "2020-04-08T17:17Z",
  "claimType": "Click",
  "adGroupId": 1234567890,
  "countryOrRegion": "US",
  "keywordId": 123222,
  "adId": 542317136,
  "supplyPlacement": "APPSTORE_SEARCH_RESULTS"
}
```

##### Tap Through Payload Example

A payload for tap-through attribution resembles the following:

```json
{
  "attribution": true,
  "orgId": 40669820,
  "campaignId": 542370539,
  "conversionType": "Download",
  "clickDate": "2024-10-08T17:17Z",
  "claimType": "Click",
  "adGroupId": 542317095,
  "countryOrRegion": "US",
  "keywordId": 87675432,
  "adId": 542317136,
  "supplyPlacement": "APPSTORE_SEARCH_RESULTS"
}
```

##### View Through Payload Example

A payload for view-through attribution resembles the following:

```json
{
  "attribution": true,
  "orgId": 40669820,
  "campaignId": 542370539,
  "conversionType": "Download",
  "impressionDate": "2024-10-08T17:17Z",
  "claimType": "Impression",
  "adGroupId": 542317095,
  "countryOrRegion": "US",
  "keywordId": 87675432,
  "adId": 542317136,
  "supplyPlacement": "APPSTORE_SEARCH_RESULTS"
}
```

##### Pre Order Payload Example

A payload for pre-order attribution on tap-throughs resembles the following:

```json
{
  "attribution": true,
  "orgId": 40669820,
  "campaignId": 542370539,
  "conversionType": "PreOrder",
  "clickDate": "2020-04-08T17:17Z",
  "claimType": "Click",
  "adGroupId": 542317095,
  "countryOrRegion": "US",
  "keywordId": 87675432,
  "adId": 542317136,
  "supplyPlacement": "APPSTORE_SEARCH_RESULTS"
}
```

A payload for pre-order attribution on view-throughs resembles the following:

```json
{
  "attribution": true,
  "orgId": 40669820,
  "campaignId": 542370539,
  "conversionType": "PreOrder",
  "impressionDate": "2020-04-08T17:17Z",
  "claimType": "Impression",
  "adGroupId": 542317095,
  "countryOrRegion": "US",
  "keywordId": 87675432,
  "adId": 542317136,
  "supplyPlacement": "APPSTORE_SEARCH_RESULTS"
}
```

#### Attribution Payload Descriptions

| **Field** | **Data type** | **Description** |
| --- | --- | --- |
| `adGroupId` | long | The identifier for the ad group. ![None](/images/com.apple.AdServices/spacer.png)Use [`Ad Groups Report`](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-ad-group-reports) to correlate your attribution response by `adGroupId` and its corresponding campaign in the Apple Ads Platform API. |
| `adId` | long | The identifier representing the assignment relationship between an `ad` object and an ad group. This ID applies to devices running iOS 15.2 and later. ![None](/images/com.apple.AdServices/spacer.png)Use [`Ads Report`](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-ad-reports) to correlate your attribution response by `adId` in the Apple Ads Platform API. |
| `attribution` | boolean | The attribution value. A value of `true` returns if a user clicks an Apple Ads impression up to 30 days before your app download or views it within 24 hours. If the API can’t find a matching attribution record, the attribution value is `false`. ![None](/images/com.apple.AdServices/spacer.png) Note: campaigns with age and gender targeting criteria return a value of `false`. See `claimType` for more details. |
| `campaignId` | long | The unique identifier for the campaign. ![None](/images/com.apple.AdServices/spacer.png)Use [`Campaigns Report`](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-campaign-reports) in the Apple Ads Platform API to correlate your attribution response by `campaignId`. |
| `claimType` | string | For view-through attribution, `claimType` will have a value of `Impression` to indicate users who viewed an ad in a corresponding Apple Ads campaign but didn’t tap on it, within 24 hours of an ad view. ![None](/images/com.apple.AdServices/spacer.png)For tap-through attribution, `claimType` will have a value of `Click`, specifying that the user tapped on an ad. ![None](/images/com.apple.AdServices/spacer.png)Note: the tap-through attribution window is 30 days and tap-through attribution is prioritized over view-through attribution. |
| `clickDate` | date/time string | The date and time when the user clicks an ad in a corresponding campaign. ![None](/images/com.apple.AdServices/spacer.png)This field only appears in the attribution response payload. |
| `conversionType` | string | The type of conversion. Values are `Download`, `Redownload` or `PreOrder`. The `PreOrder` value attributes both clicks and views. If a pre-order was placed within 30 days from the click or 1 day from the view, the lookback window for click-throughs is 90 days. The lookback window for view-throughs is 61 days. ![None](/images/com.apple.AdServices/spacer.png)Conversion types appear in your [`AppsCampaignMetrics`](https://developer.apple.comhttps://developer.apple.com/documentation/apple-ads-platform-api/appscampaignmetrics) in the Apple Ads Platform API. |
| `countryOrRegion` | string | The country or region for the campaign. ![None](/images/com.apple.AdServices/spacer.png)Refer to the `groupBy` section of the [`AppsReportingRequest`](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingrequest) in the Apple Ads Platform API for more details. |
| `impressionDate` | UTC string | Represents the date and time when an ad view occurs in a corresponding Apple Ads campaign. The `impressionDate` attribute appears in the view-through attribution response payload. |
| `keywordId` | long | The identifier for the keyword. ![None](/images/com.apple.AdServices/spacer.png)Use [`Keywords Report`](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-keyword-reports) in the Apple Ads Platform API to correlate your attribution response by `keywordId`. ![None](/images/com.apple.AdServices/spacer.png)Note, when you enable search match, the API doesn’t return `keywordId` in the attribution response. ![None](/images/com.apple.AdServices/spacer.png)See [`Ad Groups Endpoints`](https://developer.apple.com/documentation/apple-ads-platform-api/adgroups-endpoints) for more information. |
| `orgId` | long | The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in Apple Ads Advanced. ![None](/images/com.apple.AdServices/spacer.png)Obtain your `orgId` by calling [`Get User ACL`](https://developer.apple.com/documentation/apple-ads-platform-api/get-user-acls) in the Apple Ads Platform API. |
| `supplyPlacement` | string | The ad placements for a campaign. |

##### Supplyplacement Descriptions

| **Value** | **Description** |
| --- | --- |
| `APPSTORE_PRODUCT_PAGES` | Product page ads on the App Store allow you to reach users browsing app pages, appearing at the top of the “You Might Also Like” list when users scroll to the bottom. |
| `APPSTORE_SEARCH_RESULTS` | Search results ads let you reach users when they search for something specific, with an ad in relevant search results. |
| `APPSTORE_SEARCH_TAB` | Search tab ads let you reach users before they search for something specific, with an ad that appears prominently at the top of the suggested apps list on the Search tab. |
| `APPSTORE_TODAY_TAB` | Today tab ads let you reach people on the front page of the App Store, where users start their visit. |


---

*[View on Apple Developer](https://developer.apple.com/documentation/adservices/aaattribution/attributiontoken())*