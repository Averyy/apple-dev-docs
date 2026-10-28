# denyInAppPurchases

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to deny the user permission to make in-app purchases.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var denyInAppPurchases: Bool? { get set }
```

## Discussion

If your app doesn’t constrain this setting, the value is `nil`.

## See Also

### Denying In-App Purchases
- [static let denyInAppPurchases: SettingMetadata<Bool>](./denyinapppurchases-swift.type.property.md)
  The metadata associated with the setting to deny in-app purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/appstoresettings/denyinapppurchases-swift.property)*