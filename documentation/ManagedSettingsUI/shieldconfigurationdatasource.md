# ShieldConfigurationDataSource

**Framework**: Managed Settings UI  
**Kind**: class  
**Role**: Class

The base class for the principal object of an app extension that configures a shield’s appearance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@objc
class ShieldConfigurationDataSource
```

#### Overview

You can create an extension to customize the appearance of the shields that the system uses to cover an application or website. The system provides your extension with the display names, bundle identifiers, and domains for each application, website, or category it shields. Your extension is expected to return an appropriate configuration as quickly as possible, in order to provide the best possible user experience. To protect the Family Sharing group’s privacy, your extension runs in a sandbox. This sandbox prevents your extension from making network requests or moving sensitive content outside the extension’s address space. The system provides a default appearance for any methods that your subclass doesn’t override, or if it takes too long to return a configuration.

## Topics

### Styling an application shield
- [func configuration(shielding: Application) -> ShieldConfiguration](./shieldconfigurationdatasource/configuration%28shielding%29-5uqm1.md)
  Requests a configuration to use for a shield that covers an application.
- [func configuration(shielding: Application, in: ActivityCategory) -> ShieldConfiguration](./shieldconfigurationdatasource/configuration%28shielding,in%29-ia14.md)
  Requests a configuration to use for a shield that covers an application because of its category.
### Styling a website shield
- [func configuration(shielding: WebDomain) -> ShieldConfiguration](./shieldconfigurationdatasource/configuration%28shielding%29-18i24.md)
  Requests a configuration to use for a shield that covers a website.
- [func configuration(shielding: WebDomain, in: ActivityCategory) -> ShieldConfiguration](./shieldconfigurationdatasource/configuration%28shielding,in%29-6n6rd.md)
  Requests a configuration to use for a shield that covers a website because of its category.
### Initializers
- [init()](./shieldconfigurationdatasource/init%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Shield appearance
- [struct ShieldConfiguration](./shieldconfiguration.md)
  An object that defines the appearance of a shield to display over an application or website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource)*