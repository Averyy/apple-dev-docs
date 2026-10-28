# NSPinnedDomains

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

A collection of certificates that App Transport Security expects when connecting to named domains.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+

## Details

- **Name**: `NSPinnedDomains`
- **Type**: dictionary

## Discussion

The value for this optional key is a dictionary with keys that specify the domain names for which you want to set the expected certificates. The value for each domain name key is another dictionary that configures the expected certificates for that domain.

```console
NSPinnedDomains : Dictionary {
    <domain-name-string> : Dictionary {
        NSIncludesSubdomains : Boolean
        NSPinnedCAIdentities : Array
        NSPinnedLeafIdentities : Array
    }
}
```

For any domain that you specify, you must include one or more expected Certificate Authority (CA) or sub-CA certificates as the value for the [`NSPinnedCAIdentities`](../nspinnedcaidentities.md) key, one or more expected leaf certificates as the value for the [`NSPinnedLeafIdentities`](../nspinnedleafidentities.md) key, or both. If you specify both, App Transport Security (ATS) requires a match in each category.

To specify a domain name string, follow the rules for domain names given in [`NSExceptionDomains`](./nsexceptiondomains.md). You can also extend the pinning to cover subdomains by setting the value for the [`NSIncludesSubdomains`](../nsincludessubdomains.md) key to `YES`.

Pinning a certificate for a given domain has no impact on other security requirements or configuration. For example, pinning a CA certificate doesn’t change the way the system evaluates that certificate’s suitability as an anchor certificate. For information about securing network connections, see [Preventing Insecure Network Connections](../../../Security/preventing-insecure-network-connections.md).

## Topics

### Subdomains
- [NSIncludesSubdomains](../nsincludessubdomains.md)
  A Boolean value that indicates whether to extend the configuration to subdomains of the given domain.
### Identities
- [NSPinnedCAIdentities](../nspinnedcaidentities.md)
  A list of allowed Certificate Authority certificates for a given domain name.
- [NSPinnedLeafIdentities](../nspinnedleafidentities.md)
  A list of allowed leaf certificates for a given domain name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nspinneddomains)*