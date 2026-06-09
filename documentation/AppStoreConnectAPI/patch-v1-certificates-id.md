# Modify a Certificate

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the activation status for a specific certificate.

**Availability**:
- App Store Connect API 3.8+

## Mentions

- [App Store Connect API 3.8 release notes](app-store-connect-api-3-8-release-notes.md)
- [Managing merchant IDs and Payment Processing certificates](managing-payment-processing-certificates.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/certificates/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List and download certificates`](get-v1-certificates.md) response.

## See Also

- [Create a certificate](post-v1-certificates.md)
  Create a new certificate using a certificate signing request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-certificates-_id_)*