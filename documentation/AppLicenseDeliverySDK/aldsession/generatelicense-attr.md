# generateLicense(attr:)

**Framework**: App License Delivery SDK  
**Kind**: method

Generates a license based on the provided ALDLicenseAttribute and add it to the session. Multiple licenses can be generated in this session by callling this function multiple times, they get added to the session response.

## Declaration

```swift
func generateLicense(attr: ALDLicenseAttribute) throws
```

## Mentions

- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)

## Parameters

- `attr`: And ALDLicenseAttribute describing the terms of the license and the key objects


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldsession/generatelicense(attr:))*