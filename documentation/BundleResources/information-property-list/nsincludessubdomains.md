# NSIncludesSubdomains

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether to extend the configuration to subdomains of the given domain.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

#### Discussion

You can include this key in any of the domain-specific dictionaries that you add to the [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) and [`NSPinnedDomains`](information-property-list/nsapptransportsecurity/nspinneddomains.md) dictionaries. Adding the [`NSIncludesSubdomains`](information-property-list/nsincludessubdomains.md) key affects the applicability of the other configuration in the same domain-specific dictionary. The key is optional, with a default value of `NO`.

Set the value for this key to `YES` to apply the configuration for the given domain to all subdomains of the domain that have one additional path component. For example, if you set this value to `YES` and the domain name string is `example.com`, then the configuration applies to `example.com`, as well as `math.example.com` and `history.example.com`. However, it doesn’t apply to the subdomains `advanced.math.example.com` or `ancient.history.example.com` because those subdomains have two additional path components. If the value is `NO` the configuration applies only to `example.com`.

If you create an [`NSExceptionDomains`](information-property-list/nsapptransportsecurity/nsexceptiondomains.md) dictionary for an IP address or a range of addresses, the [`NSIncludesSubdomains`](information-property-list/nsincludessubdomains.md) key has no effect for that exception.

## See Also

- [NSExceptionDomains](information-property-list/nsapptransportsecurity/nsexceptiondomains.md)
  Custom App Transport Security (ATS) configurations for named domains.
- [NSPinnedDomains](information-property-list/nsapptransportsecurity/nspinneddomains.md)
  A collection of certificates that App Transport Security expects when connecting to named domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsincludessubdomains)*