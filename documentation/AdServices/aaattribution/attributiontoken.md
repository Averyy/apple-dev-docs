# attributionToken()

**Framework**: Adservices  
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

## Mentions

- [Changelog](changelog.md)

#### Discussion

The token that the framework returns is a Base64 encoded string and has a 24-hour TTL. You can provide the token to a Mobile Measurement Provider ( MMP), or app developers can use it to make a `POST` API call to fetch attribution records within the 24-hour TTL window. Use a single token in the request body and use a content-type of `text/plain` in the header, as the following example shows:

```other
POST https://api-adservices.apple.com/api/v1/
--header 'Content-Type: text/plain' \
--data-raw

G9i5hC8lQJeGOfmS+MFycll/025oJEjtpZ+rs4AUkDEJh52fT8RrjwIR/ h+2JOpXz4MRdmtcemL8WTTHfNN52tjqjbWupke40AAAAVADAAAAvQAAAIAg QF1+XF4Tl2IZ7Bw/M6ufUHt+UcIhuBeJT8YenB2v36bnZKEjvq/ IH8rqXkRELTHdyiqOYtpy837+UjF/NjE6t1/ l7sIn71b0t3FEXJd8QOtl3Bi6iQyJgGeN8w8X0MK1PDqz9nLJtRD/ wl+p112qR2YrMDyyKnwNrbfRhnGB9AAAAB7wAXlwNHelWf5RT2bzSJcGflq ELMCGoDEHIl7jF6kAAACfAb9ylY8ffdbTlyJODQYQ/ 6V9qbaBAAAAhgUBW39MQI1A0SZgNmZFz4KPaF94BxBzd4rDkjr/ eSeuaXWCmEW3ZhBzE/MOM17hAPBVlDhTPcZ/2ybr3WYIkfb+AAg/ 7jxGpDXgTtco3fzTytnZpEaI5SenXHALIexQAUTBsfBW2HCMQuTRo+7anoW kf69656ZAWcSc3DEQ1CAkUSKO9X7iAAABBEQQBQA=
```

> ❗ **Important**: A 404 response can occur if you make an API call too quickly after receiving a valid token. A best practice is to initiate retries at intervals of 5 seconds, with a maximum of three attempts.

For details about error codes, see [`AAAttributionError`](aaattributionerror.md).

##### Response Codes

|  |  |
| --- | --- |
| 200 | Success. If the API finds a matching attribution record, the payload returns `attribution=true`. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)If the API doesn’t find a matching attribution record, the payload returns `attribution=false`. In this case, the `200` `OK` response is acknowledgment of the receipt of the data request. |
| 400 | The token is invalid. |
| 404 | Not found. The API is unable to retrieve the requested attribution record.  ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Tokens have a TTL of 24 hours. If the `POST` API call exceeds 24 hours, a `404` response returns. If your token is valid, a best practice is to initiate retries at intervals of 5 seconds with a maximum of three attempts. |
| 500 | The Apple Search Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later. |

##### Attribution Payload

The API returns two types of attribution records: a standard response and a detailed response.

In iOS 14 and later, the Allow Apps to Request to Track (AAtRtT) device-level setting determines the response that the attribution server returns, as well as the details that are available from the attribution payload. The AAtRtT setting allows users to opt in or out of allowing apps to request user consent to access app-related data for both attribution and tracking the user or the device. The following table shows the combination of tracking interactions and expected attribution payload response:

|  |  |  |
| --- | --- | --- |
| On | Unknown ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)[`ATTrackingManager.AuthorizationStatus.notDetermined`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/notDetermined) | Standard |
| On | Denied or restricted ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)[`ATTrackingManager.AuthorizationStatus.denied`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/denied) / ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)[`ATTrackingManager.AuthorizationStatus.restricted`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/restricted) | Standard |
| On | Authorized ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)[`ATTrackingManager.AuthorizationStatus.authorized`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/authorized) | Detailed |
| Off | Unknown ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)[`ATTrackingManager.AuthorizationStatus.notDetermined`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/notDetermined) | Standard |
| Off | Denied or restricted ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)[`ATTrackingManager.AuthorizationStatus.denied`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/denied) / ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)[`ATTrackingManager.AuthorizationStatus.restricted`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/restricted) | Standard |
| Off | Authorized ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)[`ATTrackingManager.AuthorizationStatus.authorized`](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus/authorized) | Detailed |

The attribution record is a data dictionary with key-value pairs that correspond to your Apple Search Ads campaigns and app downloads on Apple News and Stocks from devices running iOS 14 and later. For more information, see [`Changelog`](changelog.md).

A detailed payload for tap-through attribution resembles the following:

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
  "adId": 542317136
}
```

A standard payload for tap-through attribution resembles the following:

```json
{
  "attribution": true,
  "orgId": 40669820,
  "campaignId": 542370539,
  "conversionType": "Download",
  "claimType": "Click",
  "adGroupId": 542317095,
  "countryOrRegion": "US",
  "keywordId": 87675432,
  "adId": 542317136
}
```

A detailed payload for view-through attribution resembles the following:

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
  "adId": 542317136
}
```

A standard payload for view-through attribution resembles the following:

```json
{
  "attribution": true,
  "orgId": 40669820,
  "campaignId": 542370539,
  "conversionType": "Download",
  "claimType": "Impression",
  "adGroupId": 542317095,
  "countryOrRegion": "US",
  "keywordId": 87675432,
  "adId": 542317136
}
```

> **Note**: If you receive test data in your payload responses, check to make sure your app isn’t in developer mode.

Run reports to review detailed campaign metadata in [`Apple Search Ads`](https://developer.apple.com/documentation/apple_search_ads) or [`Apple Search Ads Advanced`](https://developer.apple.comhttps://searchads.apple.com/advanced/).

##### Attribution Payload Descriptions

|  |  |  |
| --- | --- | --- |
| `adGroupId` | Integer | The identifier for the ad group. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Use [`Get Ad Group-Level Reports`](https://developer.apple.com/documentation/apple_search_ads/Get-Ad-Group-Level-Reports) to correlate your attribution response by `adGroupId` and its corresponding campaign in the Apple Search Ads Campaign Management API. |
| `adId` | Integer | The identifier representing the assignment relationship between an `ad` object and an ad group. This applies to devices running iOS 15.2 and later. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Use [`Get Ad Group-Level Reports`](https://developer.apple.com/documentation/apple_search_ads/Get-Ad-Group-Level-Reports) to correlate your attribution response by `adId` in the Apple Search Ads Campaign Management API. |
| `attribution` | Boolean | The attribution value. A value of `true` returns if a user clicks an Apple Search Ads impression up to 30 days before your app download. If the API can’t find a matching attribution record, the attribution value is `false`. |
| `campaignId` | Integer | The unique identifier for the campaign. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Use [`Get Campaign-Level Reports`](https://developer.apple.com/documentation/apple_search_ads/Get-Campaign-Level-Reports) in the Apple Search Ads Campaign Management API to correlate your attribution response by `campaignId`. |
| `claimType` | string | Returned in both standard and detailed payloads: ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)For view-through attribution, `claimType` will have a value of `Impression` to indicate users who viewed an ad in a corresponding Apple Search Ads campaign but didn’t tap on it, within 24 hours of an ad view. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png) Note: for view-through attribution, campaigns with age and gender targeting criteria return a value of `false`. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)For tap-through attribution, `claimType` will have a value of `Click`, specifying that the user tapped on an ad. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Note: the tap-through attribution window is 30 days and tap-through attribution is prioritized over view-through attribution. |
| `clickDate` | Date/Time string | The date and time when the user clicks an ad in a corresponding campaign. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)This field only appears in the detailed attribution response payload. |
| `conversionType` | String | The type of conversion is either `Download` or `Redownload`. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Conversion types appear in your campaign reports in the Apple Search Ads Campaign Management API. See the [`ExtendedSpendRow`](https://developer.apple.com/documentation/apple_search_ads/ExtendedSpendRow) object for more information. |
| `countryOrRegion` | String | The country or region for the campaign. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Use [`Get Campaign-Level Reports`](https://developer.apple.com/documentation/apple_search_ads/Get-Campaign-Level-Reports) to correlate your attribution response by `countryOrRegion` in the Apple Search Ads Campaign Management API. |
| `impressionDate` | UTC string | Represents the date and time when an ad view occurs in a corresponding Apple Search Ads campaign. The `impressionDate` attribute only appears in the detailed ad view-through attribution response payload. |
| `keywordId` | Integer | The identifier for the keyword. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Use [`Get Keyword-Level Reports`](https://developer.apple.com/documentation/apple_search_ads/Get-Keyword-Level-Reports) in the Apple Search Ads Campaign Management API to correlate your attribution response by `keywordId`. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Note, when you enable search match, the API doesn’t return `keywordId` in the attribution response. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)See [`Ad Groups`](https://developer.apple.com/documentation/Apple_Search_Ads/ad-groups) for more information. |
| `orgId` | Integer | The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in the Apple Search Ads UI. ![None](https://docs-assets.developer.apple.com/published/e5f51b2395970bdf7acf42b6603b53c9/spacer.png)Obtain your `orgId` by calling [`Get User ACL`](https://developer.apple.com/documentation/apple_search_ads/Get-User-ACL) in the Apple Search Ads Campaign Management API. |


---

*[View on Apple Developer](https://developer.apple.com/documentation/adservices/aaattribution/attributiontoken())*