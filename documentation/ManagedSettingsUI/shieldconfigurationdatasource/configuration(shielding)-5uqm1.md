# configuration(shielding:)

**Framework**: Managed Settings UI  
**Kind**: method  
**Role**: Instance Method

Requests a configuration to use for a shield that covers an application.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func configuration(shielding application: Application) -> ShieldConfiguration
```

## Return Value

The shield to display.

## Parameters

- `application`: The application the shield covers.

## See Also

### Styling an application shield
- [func configuration(shielding: Application, in: ActivityCategory) -> ShieldConfiguration](./configuration%28shielding,in%29-ia14.md)
  Requests a configuration to use for a shield that covers an application because of its category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource/configuration(shielding:)-5uqm1)*