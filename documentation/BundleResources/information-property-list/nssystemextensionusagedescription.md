# NSSystemExtensionUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells people why the app is trying to install a system extension bundle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

#### Discussion

This key is required for all system extensions except [`DriverKit`](https://developer.apple.com/documentation/DriverKit) extensions. Failure to include this key results in an error at activation time. For DriverKit extensions, use [`OSBundleUsageDescription`](information-property-list/osbundleusagedescription.md) instead.

## See Also

- [OSBundleUsageDescription](information-property-list/osbundleusagedescription.md)
  A message that tells people why the app is trying to install a driver extension bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nssystemextensionusagedescription)*