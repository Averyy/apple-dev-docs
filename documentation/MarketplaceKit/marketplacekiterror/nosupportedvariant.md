# MarketplaceKitError.noSupportedVariant

**Framework**: MarketplaceKit  
**Kind**: case  
**Role**: Case

An error that indicates the requested app doesn’t have a supported variant for this device.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case noSupportedVariant
```

## See Also

### Device and platform compatibility errors
- [MarketplaceKitError.minimumPlatformVersionNotSatisfied(_:)](./minimumplatformversionnotsatisfied%28_%29.md)
  An error that indicates the device has a lower platform version than that required by the requested app.
- [MarketplaceKitError.missingCapabilities(_:)](./missingcapabilities%28_%29.md)
  An error that indicates the device lacks capabilities that requested app requires.
- [MarketplaceKitError.unsupportedPlatform](./unsupportedplatform.md)
  An error that indicates that the requested app doesn’t support the platform.
- [case insufficientStorageSpace(Measurement<UnitInformationStorage>)](./insufficientstoragespace%28_%29.md)
  An error that indicates that the device lacks the required disk space to install the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacekiterror/nosupportedvariant)*