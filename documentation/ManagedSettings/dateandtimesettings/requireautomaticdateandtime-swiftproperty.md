# requireAutomaticDateAndTime

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether to prevent the user from changing their device’s date and time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var requireAutomaticDateAndTime: Bool? { get set }
```

#### Discussion

If your app doesn’t configure this setting, the value is `nil`.

## See Also

- [static let requireAutomaticDateAndTime: SettingMetadata<Bool>](dateandtimesettings/requireautomaticdateandtime-swift.type.property.md)
  The metadata for the constraint that configures the date and time setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/dateandtimesettings/requireautomaticdateandtime-swift.property)*