# NetworkDNSSettingsOnDemandRulesElement_ActionParameterObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that provides per-connection rules.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkDNSSettingsOnDemandRulesElement_ActionParameterObject
```

#### Discussion

The keys allowed in each dictionary are described below. Note: This array is only for dictionaries in which `EvaluateConnection` is the `Action` value.

## Properties

- `DomainAction` (string) *(required)*: The DNS settings behavior for the specified domains. Allowed values: - ‘NeverConnect’: Don’t use the DNS Settings for the specified domains.
- ‘ConnectIfNeeded’: Allow using the DNS Settings for the specified domains.
- `Domains` ([string]) *(required)*: The domains for which this evaluation applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkdnssettingsondemandruleselement_actionparameterobject)*