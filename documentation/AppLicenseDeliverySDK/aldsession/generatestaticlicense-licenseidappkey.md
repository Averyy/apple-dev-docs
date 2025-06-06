# generateStaticLicense(licenseID:appKey:)

**Framework**: App License Delivery SDK  
**Kind**: method

Generates a static license based on the provided ALDLicenseAttribute. This method produces a static license, in a bytes array. A static license is a minimal license that is only used to install apps on the device and is not meant to enforce marketplace defined rights.

## Declaration

```swift
func generateStaticLicense(licenseID: UInt64, appKey: ALDAppKey) throws
```

## Parameters

- `licenseID`: licenseID chosen for the license
- `appKey`: The app key provided for the specified app


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldsession/generatestaticlicense(licenseid:appkey:))*