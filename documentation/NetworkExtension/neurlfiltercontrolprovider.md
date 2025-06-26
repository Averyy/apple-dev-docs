# NEURLFilterControlProvider

**Framework**: Network Extension  
**Kind**: protocol

A protocol that defines an object that’s responsible for fetching pre-filter data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
protocol NEURLFilterControlProvider : AppExtension
```

#### Overview

Create a class that conforms to this protocol in your app extension, then provide the extension’s bundle identifier to the [`NEURLFilterManager`](neurlfiltermanager.md) in [`setConfiguration(pirServerURL:pirPrivacyPassIssuerURL:pirAuthenticationToken:controlProviderBundleIdentifier:)`](neurlfiltermanager/setconfiguration(pirserverurl:pirprivacypassissuerurl:pirauthenticationtoken:controlproviderbundleidentifier:).md).

## Topics

### Starting and stopping the provider
- [func start() async throws](neurlfiltercontrolprovider/start.md)
  Prepares the filter to start, in response to a call from the framework.
- [func stop(reason: NEProviderStopReason) async throws](neurlfiltercontrolprovider/stop(reason:).md)
  Prepares the filter to stop, in response to a call from the framework.
### Fetching a prefilter
- [func fetchPrefilter() async throws -> NEURLFilterPrefilter?](neurlfiltercontrolprovider/fetchprefilter.md)
  Fetches pre-filter data, in response to a call from the framework.
- [struct NEURLFilterPrefilter](neurlfilterprefilter.md)
  A structure containing a prefilter returned by a filter control provider.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [class NEURLFilterManager](neurlfiltermanager.md)
  A class you use to configure and control a URL filter.
- [class NEURLFilterControlProviderConfiguration](neurlfiltercontrolproviderconfiguration.md)
  A class that defines app extension configurations for the URL Filter control provider app extension.
- [class NEURLFilter](neurlfilter.md)
  A class used to voluntarily validate URLs for apps that don’t use WebKit or the URL session API.
- [Filtering traffic by URL](filtering-traffic-by-url.md)
  Perform fast and robust filtering of full URLs by managing URL filtering configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolprovider)*