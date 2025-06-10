# NEDNSProxyManager

**Framework**: Network Extension  
**Kind**: class

An object to create and manage an DNS proxy provider’s configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEDNSProxyManager
```

#### Overview

A DNS proxy allows your app to intercept all DNS traffic generated on a device. You can use this capability to provide services like DNS traffic encryption, typically by redirecting DNS traffic to your own server. You usually do this in the context of managed devices, such as those owned by a school or an enterprise.

You create a DNS proxy as an app extension based on a custom subclass of the [`NEDNSProxyProvider`](nednsproxyprovider.md) class. You enable and configure this proxy from within your app using the singleton proxy manager instance provided by the [`shared()`](nednsproxymanager/shared().md) type method of the [`NEDNSProxyManager`](nednsproxymanager.md) class. For example, for a proxy that performs a simple redirect, you can use the proxy manager to define and dynamically configure the destination IP address of the redirected traffic.

Instances of the proxy manager are thread safe.

> ❗ **Important**:  To use the [`NEDNSProxyManager`](nednsproxymanager.md) class, you must enable the Network Extensions capability in Xcode and select the DNS Proxy capability. See [`Configure network extensions`](https://developer.apple.comhttp://help.apple.com/xcode/mac/current/#/dev0b2ef6f08).

## Topics

### Managing the DNS proxy configuration
- [class func shared() -> NEDNSProxyManager](nednsproxymanager/shared.md)
  Returns a singleton DNS proxy manager instance.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/loadfrompreferences(completionhandler:).md)
  Loads the current DNS proxy configuration from the caller’s DNS proxy preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/savetopreferences(completionhandler:).md)
  Saves the DNS proxy configuration in the caller’s DNS proxy preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/removefrompreferences(completionhandler:).md)
  Removes the DNS proxy configuration from the caller’s DNS proxy preferences.
### Accessing DNS proxy configuration properties
- [var isEnabled: Bool](nednsproxymanager/isenabled.md)
  The status of a DNS proxy.
- [var providerProtocol: NEDNSProxyProviderProtocol?](nednsproxymanager/providerprotocol.md)
  The provider-specific portion of the DNS proxy configuration.
- [var localizedDescription: String?](nednsproxymanager/localizeddescription.md)
  A description of the DNS proxy.
### Notifications
- [static let NEDNSProxyConfigurationDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NEDNSProxyConfigurationDidChange.md)
  A notification that is posted when the DNS proxy configuration changes.
### Errors
- [let NEDNSProxyErrorDomain: String](nednsproxyerrordomain.md)
  The DNS proxy error domain.
- [enum NEDNSProxyManagerError](nednsproxymanagererror.md)
  The possible DNS proxy manager errors.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEDNSProxyProviderProtocol](nednsproxyproviderprotocol.md)
  Configuration parameters for a DNS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager)*