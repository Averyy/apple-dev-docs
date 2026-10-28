# Retention Messaging API changelog

**Framework**: Retention Messaging API  
**Role**: Article

Learn about new features and updates in the Retention Messaging API.

## Overview

Use this changelog to learn about feature updates, deprecations, and removals for the Retention Messaging API.

### Server update  — 2026/05/05

Updated recommended domain from `api.storekit.itunes.apple.com` to `api.storekit.apple.com`, and `api.storekit-sandbox.itunes.apple.com` to `api.storekit-sandbox.apple.com`. The previous domains will continue to be supported.

### 1.5 2026/04/27

**New features**

- Added the new property [`billingPlanType`](./billingplantype.md) to [`alternateProduct`](./alternateproduct.md) to support monthly subscriptions with 12-month commitments.

### 1.4  2026/03/31

**New features**

- Added [`Configure Realtime URL`](./configure-realtime-url.md), [`Get Realtime URL`](./get-realtime-url.md), [`Delete Realtime URL`](./delete-realtime-url.md), and [`Get Default Message`](./get-default-message.md) endpoints.
- Added objects, properties, and types related to the new endpoints, including: [`BulletPoint`](./bulletpoint.md), [`bulletPointText`](./bulletpointtext.md), [`headerPosition`](./headerposition.md), [`imageSize`](./imagesize.md), [`realtimeURL`](./realtimeurl.md), and [`RealtimeUrlRequest`](./realtimeurlrequest.md).
- Added [Error codes](./error-codes.md) to indicate bad requests and other errors related to the added endpoints.
- Updated [`GetImageListResponseItem`](./getimagelistresponseitem.md) and [`Upload Image`](./upload-image.md) to add support for the `imageSize` parameter.
- Updated [`UploadMessageRequestBody`](./uploadmessagerequestbody.md) to add support for the `bulletPoints` and [`headerPosition`](./headerposition.md) parameters.

### 1.3  2025/12/09

**New features**

- The framework now supports the ability to test server response times for real time retention messaging using the [`Initiate Performance Test`](./initiate-performance-test.md) and [`Get Performance Test Results`](./get-performance-test-results.md) endpoints.

### 1.2  2025/11/05

**New features**

- Updated the [`RealtimeResponseBody`](./realtimeresponsebody.md) to include the [`advancedCommerceInfo`](./advancedcommerceinfo.md) object.

### 1.1  2025/09/04

**New features**

- Updated the [`DecodedRealtimeRequestBody`](./decodedrealtimerequestbody.md) to include the [`environment`](./environment.md) and [`signedDate`](./signeddate.md) fields.

### 1.0  2025/07/16

Initial pre-release.

## See Also

### Essentials
- [Setting up retention messages](./setting-up-retention-messages.md)
  Upload images and messages for retention messaging, configure default messages, and complete the setup for promotional-offer and switch-plan messages.
- [Identifying rate limits](./identifying-rate-limits.md)
  Recognize the rate limits that apply to Retention Messaging API endpoints, and handle them in your code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/retention-messaging-changelog)*