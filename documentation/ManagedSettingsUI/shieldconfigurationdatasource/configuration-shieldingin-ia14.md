# configuration(shielding:in:)

**Framework**: ManagedSettingsUI  
**Kind**: method

Requests a configuration to use for a shield that covers an application because of its category.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func configuration(shielding application: Application, in category: ActivityCategory) -> ShieldConfiguration
```

#### Return Value

The shield to display.

## Parameters

- `application`: The application the shield covers.
- `category`: The category of the application that the shield covers.

## See Also

- [func configuration(shielding: Application) -> ShieldConfiguration](shieldconfigurationdatasource/configuration(shielding:)-5uqm1.md)
  Requests a configuration to use for a shield that covers an application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource/configuration(shielding:in:)-ia14)*