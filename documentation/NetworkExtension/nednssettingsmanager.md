# NEDNSSettingsManager

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An object you use to create and manage a DNS settings configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class NEDNSSettingsManager
```

```objc
@interface NEDNSSettingsManager : NSObject
```

## Overview

When your app starts up, access the shared instance of the DNS settings manager, and load existing settings from the preferences using [`loadFromPreferences(completionHandler:)`](./nednssettingsmanager/loadfrompreferences%28completionhandler%29.md). You can define your DNS server configuration, and persist it by calling [`saveToPreferences(completionHandler:)`](./nednssettingsmanager/savetopreferences%28completionhandler%29.md).

In order to use your DNS settings, the user needs to enable it in the Settings app on iOS or in System Preferences on macOS.

## Topics

### Managing DNS configurations
- [class func shared() -> NEDNSSettingsManager](./nednssettingsmanager/shared%28%29.md)
  Access the single instance of a DNS settings manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./nednssettingsmanager/loadfrompreferences%28completionhandler%29.md)
  Load your DNS settings configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./nednssettingsmanager/savetopreferences%28completionhandler%29.md)
  Save your DNS settings configuration to the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./nednssettingsmanager/removefrompreferences%28completionhandler%29.md)
  Remove your DNS settings configuration from the system networking preferences.
### Accessing DNS configuration properties
- [var isEnabled: Bool](./nednssettingsmanager/isenabled.md)
  A Boolean you use to query the enabled state of the DNS settings configuration.
- [var dnsSettings: NEDNSSettings?](./nednssettingsmanager/dnssettings.md)
  An object that contains the configuration settings for a DNS server.
- [var localizedDescription: String?](./nednssettingsmanager/localizeddescription.md)
  A string that contains the display name of the DNS settings configuration.
- [var onDemandRules: [NEOnDemandRule]?](./nednssettingsmanager/ondemandrules.md)
  A list of ordered rules that defines the networks on which the DNS settings will apply.
### Handling errors
- [let NEDNSSettingsErrorDomain: String](./nednssettingserrordomain.md)
  The domain for errors resulting from calls to the DNS settings manager.
- [enum NEDNSSettingsManagerError](./nednssettingsmanagererror.md)
  Error codes specific to DNS managers.

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

### DNS configuration
- [class NEDNSOverHTTPSSettings](./nednsoverhttpssettings.md)
  The DNS resolver settings for a DNS-over-HTTPS server.
- [class NEDNSOverTLSSettings](./nednsovertlssettings.md)
  The DNS resolver settings for a DNS-over-TLS server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager)*