# OSBundleUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is trying to install a driver extension bundle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Details

- **Name**: `OSBundleUsageDescription` (Privacy - Driver Extension Usage Description)
- **Type**: string

## Discussion

This key is required for all [DriverKit](../../DriverKit/DriverKit.md) extensions. Failure to include this key results in an error at activation time. For system extensions that are not DriverKit extensions, use [`NSSystemExtensionUsageDescription`](./nssystemextensionusagedescription.md) instead.

## See Also

### System Extensions
- [NSSystemExtensionUsageDescription](./nssystemextensionusagedescription.md)
  A message that tells people why the app is trying to install a system extension bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/osbundleusagedescription)*