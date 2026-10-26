# NEFilterManager

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An object to create and manage a content filter’s configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEFilterManager
```

```objc
@interface NEFilterManager : NSObject
```

#### Overview

Each app is allowed to create a single filter configuration. The [`NEFilterManager`](./nefiltermanager.md) class has a class method ([`shared()`](./nefiltermanager/shared%28%29.md)) that provides access to a single [`NEFilterManager`](./nefiltermanager.md) instance. This single instance corresponds to a single filter configuration.

The filter configuration is stored in the Network Extension preferences which are managed by the Network Extension framework. The filter configuration must be explicitly loaded into memory from the Network Extension preferences before it can be used, and any changes must be explicitly saved to the Network Extension preferences before taking effect on the system.

> ❗ **Important**:  In product builds for distribution, Network Content Filter configurations can be created only on supervised devices. During development and testing you can temporarily override this restriction by signing your build with the `get-task-allow` entitlement.

> ❗ **Important**:  To use the [`NEFilterManager`](./nefiltermanager.md) class, you must enable the Network Extensions capability in Xcode and select the Content Filter capability. See [Configure network extensions](http://help.apple.com/xcode/mac/current/#/dev0b2ef6f08).

##### Profile Configuration

Filter configurations are created using configuration profiles. See [`WebContentFilter`](../DeviceManagement/webcontentfilter.md) for more information. To specify that a filter configuration created via a profile payload is associated with a particular app (and therefore allow the app to use `NEFilterManager` to manage the configuration), the app’s bundle identifier must be set as the value of the `PluginBundleID` field in the profile payload.

##### Filter Provider Extensions

Apps that use `NEFilterManager` are required to contain two Filter Provider extensions that together perform the task of examining network content and making pass and block decisions. See the [`NEFilterControlProvider`](./nefiltercontrolprovider.md) and [`NEFilterDataProvider`](./nefilterdataprovider.md) classes for more details about these extensions.

## Topics

### Managing the filter configuration
- [class func shared() -> NEFilterManager](./nefiltermanager/shared%28%29.md)
  Access the single instance of `NEFilterManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./nefiltermanager/loadfrompreferences%28completionhandler%29.md)
  Load the filter configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./nefiltermanager/savetopreferences%28completionhandler%29.md)
  Save the filter configuration in the Network Extension preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./nefiltermanager/removefrompreferences%28completionhandler%29.md)
  Remove the filter configuration from the Network Extension preferences.
### Accessing filter configuration properties
- [var isEnabled: Bool](./nefiltermanager/isenabled.md)
  A Boolean used to toggle the enabled state of the filter.
- [var providerConfiguration: NEFilterProviderConfiguration?](./nefiltermanager/providerconfiguration.md)
  A [`NEFilterProviderConfiguration`](./nefilterproviderconfiguration.md) object containing the filter configuration settings.
- [var localizedDescription: String?](./nefiltermanager/localizeddescription.md)
  A string containing a description of the filter configuration.
### Prioritizing filters
- [var grade: NEFilterManager.Grade](./nefiltermanager/grade-swift.property.md)
  The grade of the filter, which determines when it acts relative to other filters.
- [NEFilterManager.Grade](./nefiltermanager/grade-swift.enum.md)
  A type for the grade or priority of the filter.
### Errors
- [let NEFilterErrorDomain: String](./nefiltererrordomain.md)
  The domain for errors resulting from calls to the filter manager.
- [enum NEFilterManagerError](./nefiltermanagererror.md)
  Error codes specific to filter managers.
### Notifications
- [static let NEFilterConfigurationDidChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/nefilterconfigurationdidchange.md)
  Posted after the filter configuration stored in the Network Extension preferences changes.
- [NEFilterConfigurationDidChangeNotification](./nefilterconfigurationdidchangenotification.md)
  Posted after the filter configuration stored in the Network Extension preferences changes.
### Instance Properties
- [var disableEncryptedDNSSettings: Bool](./nefiltermanager/disableencrypteddnssettings.md)

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

### Filter configuration
- [class NEFilterProviderConfiguration](./nefilterproviderconfiguration.md)
  Configuration parameters for a content filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager)*