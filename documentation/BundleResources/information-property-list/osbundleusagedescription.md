# OSBundleUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells people why the app is trying to install a driver extension bundle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

#### Discussion

This key is required for all [`DriverKit`](https://developer.apple.com/documentation/DriverKit) extensions. Failure to include this key results in an error at activation time. For system extensions that are not DriverKit extensions, use [`NSSystemExtensionUsageDescription`](information-property-list/nssystemextensionusagedescription.md) instead.

## See Also

- [NSSystemExtensionUsageDescription](information-property-list/nssystemextensionusagedescription.md)
  A message that tells people why the app is trying to install a system extension bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/osbundleusagedescription)*