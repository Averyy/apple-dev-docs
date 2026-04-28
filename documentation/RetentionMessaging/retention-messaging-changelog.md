# Retention Messaging API changelog

**Framework**: Retention Messaging API

Learn about new features and updates in the Retention Messaging API.

#### Overview

Use this changelog to learn about feature updates, deprecations, and removals for the Retention Messaging API.

##### 15 20260427

**New features**

- Added the new property [`billingPlanType`](billingplantype.md) to [`alternateProduct`](alternateproduct.md) to support monthly subscriptions with 12-month commitments.

##### 14 20260331

**New features**

- Added [`Configure Realtime URL`](configure-realtime-url.md), [`Get Realtime URL`](get-realtime-url.md), [`Delete Realtime URL`](delete-realtime-url.md), and [`Get Default Message`](get-default-message.md) endpoints.
- Added objects, properties, and types related to the new endpoints, including: [`BulletPoint`](bulletpoint.md), [`bulletPointText`](bulletpointtext.md), [`headerPosition`](headerposition.md), [`imageSize`](imagesize.md), [`realtimeURL`](realtimeurl.md), and [`RealtimeUrlRequest`](realtimeurlrequest.md).
- Added [`Error codes`](error-codes.md) to indicate bad requests and other errors related to the added endpoints.
- Updated [`GetImageListResponseItem`](getimagelistresponseitem.md) and [`Upload Image`](upload-image.md) to add support for the `imageSize` parameter.
- Updated [`UploadMessageRequestBody`](uploadmessagerequestbody.md) to add support for the `bulletPoints` and [`headerPosition`](headerposition.md) parameters.

##### 13 20251209

**New features**

- The framework now supports the ability to test server response times for real time retention messaging using the [`Initiate Performance Test`](initiate-performance-test.md) and [`Get Performance Test Results`](get-performance-test-results.md) endpoints.

##### 12 20251105

**New features**

- Updated the [`RealtimeResponseBody`](realtimeresponsebody.md) to include the [`advancedCommerceInfo`](advancedcommerceinfo.md) object.

##### 11 20250904

**New features**

- Updated the [`DecodedRealtimeRequestBody`](decodedrealtimerequestbody.md) to include the [`environment`](environment.md) and [`signedDate`](signeddate.md) fields.

##### 10 20250716

Initial pre-release.

## See Also

- [Setting up retention messages](setting-up-retention-messages.md)
  Upload images and messages for retention messaging, configure default messages, and complete the setup for promotional-offer and switch-plan messages.
- [Identifying rate limits](identifying-rate-limits.md)
  Recognize the rate limits that apply to Retention Messaging API endpoints, and handle them in your code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/retention-messaging-changelog)*