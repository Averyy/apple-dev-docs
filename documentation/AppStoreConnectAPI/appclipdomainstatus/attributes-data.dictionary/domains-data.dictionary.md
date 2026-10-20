# AppClipDomainStatus.Attributes.Domains

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Domains you associated with your App Clip.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipDomainStatus.Attributes.Domains
```

## Properties

- `domain` (string): A domain you associated with your app or App Clip.
- `errorCode` (string): A string that describes an issue that occurred when App Store Connect tried to validate the status of an associated domain.

  **Allowed Values**: `BAD_HTTP_RESPONSE`, `BAD_JSON_CONTENT`, `BAD_PKCS7_SIGNATURE`, `CANNOT_REACH_AASA_FILE`, `CROSS_SITE_REDIRECTS_FORBIDDEN`, `DNS_ERROR`, `INSECURE_REDIRECTS_FORBIDDEN`, `INVALID_ENTITLEMENT_MISSING_SECTION`, `INVALID_ENTITLEMENT_SYNTAX_ERROR`, `INVALID_ENTITLEMENT_UNHANDLED_SECTION`, `INVALID_ENTITLEMENT_UNKNOWN_ID`, `NETWORK_ERROR`, `NETWORK_ERROR_TEMPORARY`, `OTHER_ERROR`, `TIMEOUT`, `TLS_ERROR`, `TOO_MANY_REDIRECTS`, `UNEXPECTED_ERROR`
- `isValid` (boolean): A Boolean value that indicates whether App Store Connect was able to verify the configuration of the associated domain.
- `lastUpdatedDate` (date-time): The date when App Store Connect last verified the status of an associated domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdomainstatus/attributes-data.dictionary/domains-data.dictionary)*