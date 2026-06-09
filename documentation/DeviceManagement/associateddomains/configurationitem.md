# AssociatedDomains.ConfigurationItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that maps apps to their associated domains.

**Availability**:
- macOS 10.15+

## Declaration

```swift
object AssociatedDomains.ConfigurationItem
```

## Properties

- `ApplicationIdentifier` (string) *(required)*: The app identifier to associate the domains with.
- `AssociatedDomains` ([string]) *(required)*: The domains to associate with the app. Each string is in the form of `service:domain`. Use fully qualified hostnames, such as `www.example.com`. See [`Supporting associated domains`](https://developer.apple.com/documentation/Xcode/supporting-associated-domains) for more information.
- `EnableDirectDownloads` (boolean): If `true`, the system enables direct download of data for this domain instead of through a CDN. Set the entitlement value for this domain to `service:domain?mode=managed`; otherwise, the system ignores this value. Available: macOS 11+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/associateddomains/configurationitem)*