# DNSSettings.OnDemandRulesElement.ActionParameter

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A dictionary that provides per-connection rules.

**Availability**:
- iOS 14.0+ - Deprecated in 27.0
- iPadOS 14.0+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use the declarative management `com.apple.configuration.network.dns-settings` configuration.

## Declaration

```
object DNSSettings.OnDemandRulesElement.ActionParameter
```

#### Discussion

The keys allowed in each dictionary are described below. Note: This array is only for dictionaries in which `EvaluateConnection` is the `Action` value.

## Properties

- `DomainAction` (string) *(required)* *(deprecated)*: The DNS settings behavior for the specified domains. Allowed values:

  - ‘NeverConnect’: Don’t use the DNS Settings for the specified domains.
  - ‘ConnectIfNeeded’: Allow using the DNS Settings for the specified domains.

  Deprecated: iOS 27+ | iPadOS 27+ | macOS 27+ | visionOS 27+

  **Allowed Values**: `NeverConnect`, `ConnectIfNeeded`
- `Domains` ([string]) *(required)* *(deprecated)*: The domains for which this evaluation applies.

  Deprecated: iOS 27+ | iPadOS 27+ | macOS 27+ | visionOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dnssettings/ondemandruleselement/actionparameter)*