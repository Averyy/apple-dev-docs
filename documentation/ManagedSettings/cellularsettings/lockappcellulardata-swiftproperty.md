# lockAppCellularData

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether to prevent the user from changing cellular data settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var lockAppCellularData: Bool? { get set }
```

#### Discussion

Use this setting to prevent the user from changing which apps on their device can use cellular data. If your app doesn’t constrain this setting, this value is `nil`.

## See Also

- [static let lockAppCellularData: SettingMetadata<Bool>](cellularsettings/lockappcellulardata-swift.type.property.md)
  The metadata associated with the constraint that locks the cellular data setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/cellularsettings/lockappcellulardata-swift.property)*