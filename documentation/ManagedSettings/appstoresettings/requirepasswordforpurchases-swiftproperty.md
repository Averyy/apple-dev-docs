# requirePasswordForPurchases

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether to require the user’s password to make App Store transactions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var requirePasswordForPurchases: Bool? { get set }
```

#### Discussion

Specify `true` to require the user’s password for each transaction. The value is `nil` if your app doesn’t configure this setting.

## See Also

- [static let requirePasswordForPurchases: SettingMetadata<Bool>](appstoresettings/requirepasswordforpurchases-swift.type.property.md)
  The metadata associated with the setting that requires a password for App Store purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/appstoresettings/requirepasswordforpurchases-swift.property)*