# supports(_:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Type Method

Returns a Boolean that indicates whether the device supports a specific set of features.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func supports(_ features: CBCentralManager.Feature) -> Bool
```

```objc
+ (BOOL) supportsFeatures:(CBCentralManagerFeature) features;
```

## Parameters

- `features`: One or more features that you would like to check for support.

## See Also

### Inspecting Feature Support
- [CBCentralManager.Feature](./feature.md)
  An option set of device-specific features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/supports(_:))*