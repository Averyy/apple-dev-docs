# AppClipDomainStatus.Attributes.Domains

**Framework**: App Store Connect API  
**Kind**: dictionary

Domains you associated with your App Clip.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDomainStatus.Attributes.Domains
```

## Properties

- `domain` (string): A domain you associated with your app or App Clip.
- `errorCode` (string): A string that describes an issue that occurred when App Store Connect tried to validate the status of an associated domain.
- `isValid` (boolean): A Boolean value that indicates whether App Store Connect was able to verify the configuration of the associated domain.
- `lastUpdatedDate` (date-time): The date when App Store Connect last verified the status of an associated domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdomainstatus/attributes-data.dictionary/domains-data.dictionary)*