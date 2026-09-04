# Changelog

**Framework**: AdServices

A log of Ad Services framework updates.

#### Overview

| Release date | Release details |
| --- | --- |
| September, 2026 | Attribution payload will return `attribution = false` for campaigns using age or gender targeting. |
| January, 2026 | A new `supplyPlacement` field has been added to attribution payloads, indicating the ad placement for an Apple Ads campaign. |
| November, 2025 | Apple News is unsupported in iOS 26.1 and later. |
| October, 2025 | Introduced attribution support for pre-order app campaigns. Updated the `conversionType` field with a new `preorder` value and an attribution window for both clicks and views. If a pre-order was placed within 30 days from the click or 1 day from the view the lookback window for click-throughs is 90 days. The lookback window for view-throughs is 61 days. |
| March, 2025 | Introduced view-through attribution on March 27, 2025.  A new attribute, `impressionDate` has been added to payloads for view-through attribution. A new value has been added to the `claimType` field. |
| November, 2024 | The `claimType` attribute with a value of `Click`, specifying that the app download was from a tap on an ad. Note that the tap-through attribution window is 30 days. |
| May, 2024 | To reduce the rate of delayed attribution responses resulting in 404 errors, the Ad Services API will hold connections for up to 1 second before responding with a 404 error code. Doing this allows more time for the request to be processed and correct data delivered as a part of the response, increasing the number of successful API requests. The impact on the API caller could result in an increased number of client-side connection timeouts in cases if timeout is configured for less than 1 second. |
| March, 2023 | Updated `AdServices` workflow and `AAAttribution/attributionToken()`. |
| October, 2022 | Updated `adId` description. |
| January, 2022 | Apple Ads no longer supports Creative Sets and `AdGroupCreativeSets`.  Creative Sets API calls return 200 OK responses with an invalid state. Your Creative Sets data remains available through the `AdServices` attribution framework for devices running iOS versions earlier than 15.2 where `creativeSetId` returns in payloads. For devices running iOS version 15.2 and later, `adId` returns in campaigns using a `supplySource` of `APPSTORE_TODAY_TAB` or `APPSTORE_SEARCH_RESULTS`. |


---

*[View on Apple Developer](https://developer.apple.com/documentation/adservices/changelog)*