# com.apple.developer.fileprovider.testing-mode

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether you can place domains in testing mode.

**Availability**:
- macOS 11.3+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.fileprovider.testing-mode`
- **Type**: boolean

#### Discussion

You must add this entitlement to your target before assigning a non-empty value to a domain’s [`testingModes`](../../FileProvider/nsfileproviderdomain/testingmodes-swift.property.md) property. You can only use this entitlement during testing and development. If you add it to your app or extension, you must remove it before you submit your app to TestFlight or the Mac App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.fileprovider.testing-mode)*