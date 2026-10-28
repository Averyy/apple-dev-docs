# configuration(shielding:in:)

**Framework**: Managed Settings UI  
**Kind**: method  
**Role**: Instance Method

Requests a configuration to use for a shield that covers a website because of its category.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func configuration(shielding webDomain: WebDomain, in category: ActivityCategory) -> ShieldConfiguration
```

## Return Value

The shield to display.

## Parameters

- `webDomain`: The website that the shield covers.
- `category`: The category of the website that the shield covers.

## See Also

### Styling a website shield
- [func configuration(shielding: WebDomain) -> ShieldConfiguration](./configuration%28shielding%29-18i24.md)
  Requests a configuration to use for a shield that covers a website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource/configuration(shielding:in:)-6n6rd)*