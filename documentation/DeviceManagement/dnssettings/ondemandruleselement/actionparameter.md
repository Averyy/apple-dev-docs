# DNSSettings.OnDemandRulesElement.ActionParameter

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that provides per-connection rules.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DNSSettings.OnDemandRulesElement.ActionParameter
```

#### Discussion

The keys allowed in each dictionary are described below. Note: This array is only for dictionaries in which `EvaluateConnection` is the `Action` value.

## Properties

- `DomainAction` (string) *(required)*: The DNS settings behavior for the specified domains. Allowed values: - ‘NeverConnect’: Don’t use the DNS Settings for the specified domains.
- ‘ConnectIfNeeded’: Allow using the DNS Settings for the specified domains.
- `Domains` ([string]) *(required)*: The domains for which this evaluation applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dnssettings/ondemandruleselement/actionparameter)*