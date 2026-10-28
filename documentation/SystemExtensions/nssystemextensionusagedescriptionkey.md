# NSSystemExtensionUsageDescriptionKey

**Framework**: System Extensions  
**Kind**: var  
**Role**: Global Variable

A message that tells the user why the app is trying to install a system extension bundle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
let NSSystemExtensionUsageDescriptionKey: String
```

```c
extern NSString * const NSSystemExtensionUsageDescriptionKey;
```

## Discussion

This key is required for all system extensions except DriverKit extensions, and must be in the extension’s `Info.plist` file. Failure to include this key results in an error at activation time. For DriverKit extensions, use [`OSBundleUsageDescriptionKey`](./osbundleusagedescriptionkey.md) instead.

## See Also

### Usage descriptions
- [let OSBundleUsageDescriptionKey: String](./osbundleusagedescriptionkey.md)
  A message that tells the user why the app is trying to install a driver extension bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/nssystemextensionusagedescriptionkey)*