# DNS settings

**Framework**: Network Extension

Create and manage a system-wide DNS configuration that uses built-in encrypted DNS protocols.

#### Overview

With the DNS Settings feature in macOS and iOS, your app can create and manage a configuration that uses one of the built-in DNS protocols: DNS-over-TLS or DNS-over-HTTPS. The user must explictly enable your configuration in order to use the server you specify.

## Topics

### Essentials
- [Network Extensions Entitlement](../BundleResources/Entitlements/com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
### DNS configuration
- [class NEDNSSettingsManager](nednssettingsmanager.md)
  An object you use to create and manage a DNS settings configuration.
- [class NEDNSOverHTTPSSettings](nednsoverhttpssettings.md)
  The DNS resolver settings for a DNS-over-HTTPS server.
- [class NEDNSOverTLSSettings](nednsovertlssettings.md)
  The DNS resolver settings for a DNS-over-TLS server.

## See Also

- [DNS proxy provider](dns-proxy-provider.md)
  Create an on-device DNS proxy using a custom protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/dns-settings)*