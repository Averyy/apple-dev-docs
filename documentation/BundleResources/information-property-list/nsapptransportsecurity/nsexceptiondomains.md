# NSExceptionDomains

**Framework**: Bundle Resources  
**Kind**: dictionary

Custom App Transport Security (ATS) configurations for named domains.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

#### Discussion

The value for this key is a dictionary with keys that name specific domains, IP addresses, or IP address ranges for which you want to set exceptions. The value for each domain key is another dictionary that indicates the exceptions for that domain.

```console
NSExceptionDomains : Dictionary {
    <domain-name-or-ip-address-string> : Dictionary {
        NSIncludesSubdomains : Boolean
        NSExceptionAllowsInsecureHTTPLoads : Boolean
        NSExceptionMinimumTLSVersion : String
        NSExceptionRequiresForwardSecrecy : Boolean
    }
}
```

Follow these rules when setting a domain name string:

-  — Use `example.com`, not `EXAMPLE.COM`.
-  — In iOS 17, iPadOS 17, and macOS 14, you can use an IPv4 address, for example `192.168.42.63`, or an IPv6 address, for example `2001:db8:12::34`. You can also use a classless inter-domain routing (CIDR) range, for example `2001:db8:12::/48`. For information about how ATS handles IP addresses, see [`NSAllowsLocalNetworking`](information-property-list/nsapptransportsecurity/nsallowslocalnetworking.md).

> **Note**:  If you exclude a DNS domain name and your app contacts a host by IP address, the ATS exclusion for the domain name doesn’t apply to the connection even if a DNS query for the domain name would resolve to the IP address. If you exclude an IP address and your app contacts a host by DNS name that resolves to that IP address, the ATS exclusion for the IP address doesn’t apply to the connection.

 If you exclude a DNS domain name and your app contacts a host by IP address, the ATS exclusion for the domain name doesn’t apply to the connection even if a DNS query for the domain name would resolve to the IP address. If you exclude an IP address and your app contacts a host by DNS name that resolves to that IP address, the ATS exclusion for the IP address doesn’t apply to the connection.

-  — Use `example.com`, not `example.com:443`.
-  — For example, `example.com.` (with a trailing dot) matches “example.com.” but not “example.com”. Similarly, `example.com` matches “example.com” but not “example.com.”.
-  — Don’t use `*.example.com`. Instead, use `example.com` and set [`NSIncludesSubdomains`](information-property-list/nsincludessubdomains.md) to `YES`.

The values for the keys in each individual domain’s dictionary control how ATS treats connections made to that domain.

> **Note**:  If you specify an exception domain dictionary, ATS ignores any global configuration keys, like [`NSAllowsArbitraryLoads`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md), for that domain. This is true even if you leave the domain-specific dictionary empty and rely entirely on its keys’ default values.

 If you specify an exception domain dictionary, ATS ignores any global configuration keys, like [`NSAllowsArbitraryLoads`](information-property-list/nsapptransportsecurity/nsallowsarbitraryloads.md), for that domain. This is true even if you leave the domain-specific dictionary empty and rely entirely on its keys’ default values.

## Topics

### Subdomains
- [NSIncludesSubdomains](information-property-list/nsincludessubdomains.md)
  A Boolean value that indicates whether to extend the configuration to subdomains of the given domain.
### Exceptions
- [NSExceptionAllowsInsecureHTTPLoads](information-property-list/nsexceptionallowsinsecurehttploads.md)
  A Boolean value indicating whether to allow insecure HTTP loads.
- [NSExceptionMinimumTLSVersion](information-property-list/nsexceptionminimumtlsversion.md)
  The minimum Transport Layer Security (TLS) version for network connections.
- [NSExceptionRequiresForwardSecrecy](information-property-list/nsexceptionrequiresforwardsecrecy.md)
  A Boolean value indicating whether to override the perfect forward secrecy requirement.
- [NSRequiresCertificateTransparency](information-property-list/nsrequirescertificatetransparency.md)
  An obsolete Boolean value indicating whether to require Certificate Transparency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsexceptiondomains)*