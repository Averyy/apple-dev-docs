# Modify a Beta App Review Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the details for a specific app’s beta app review.

**Availability**:
- App Store Connect API 1.0+

#### Overview

> ❗ **Important**:  First name, last name, phone, email cannot be cleared for the primary locale once set.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaAppReviewDetails/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betaappreviewdetails-_id_)*