# OSBundleUsageDescriptionKey

**Framework**: System Extensions  
**Kind**: var

A message that tells the user why the app is trying to install a driver extension bundle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
let OSBundleUsageDescriptionKey: String
```

#### Discussion

This key is required for all DriverKit extensions and must be in the extension’s `Info.plist` file. Failure to include this key results in an error at activation time. For system extensions that are not DriverKit extensions, use [`NSSystemExtensionUsageDescriptionKey`](nssystemextensionusagedescriptionkey.md) instead.

## See Also

- [let NSSystemExtensionUsageDescriptionKey: String](nssystemextensionusagedescriptionkey.md)
  A message that tells the user why the app is trying to install a system extension bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/osbundleusagedescriptionkey)*