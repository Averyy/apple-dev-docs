# MarketplaceKitError.insufficientStorageSpace(_:)

**Framework**: MarketplaceKit  
**Kind**: case

An error that indicates that the device lacks the required disk space to install the app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case insufficientStorageSpace(Measurement<UnitInformationStorage>)
```

## See Also

- [MarketplaceKitError.minimumPlatformVersionNotSatisfied(_:)](marketplacekiterror/minimumplatformversionnotsatisfied(_:).md)
  An error that indicates the device has a lower platform version than that required by the requested app.
- [MarketplaceKitError.missingCapabilities(_:)](marketplacekiterror/missingcapabilities(_:).md)
  An error that indicates the device lacks capabilities that requested app requires.
- [MarketplaceKitError.noSupportedVariant](marketplacekiterror/nosupportedvariant.md)
  An error that indicates the requested app doesn’t have a supported variant for this device.
- [MarketplaceKitError.unsupportedPlatform](marketplacekiterror/unsupportedplatform.md)
  An error that indicates that the requested app doesn’t support the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacekiterror/insufficientstoragespace(_:))*