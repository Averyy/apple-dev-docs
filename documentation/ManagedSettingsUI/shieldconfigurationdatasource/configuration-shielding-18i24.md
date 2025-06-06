# configuration(shielding:)

**Framework**: ManagedSettingsUI  
**Kind**: method

Requests a configuration to use for a shield that covers a website.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func configuration(shielding webDomain: WebDomain) -> ShieldConfiguration
```

#### Return Value

The shield to display.

## Parameters

- `webDomain`: The website that the shield covers.

## See Also

- [func configuration(shielding: WebDomain, in: ActivityCategory) -> ShieldConfiguration](shieldconfigurationdatasource/configuration(shielding:in:)-6n6rd.md)
  Requests a configuration to use for a shield that covers a website because of its category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource/configuration(shielding:)-18i24)*