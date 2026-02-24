# StatusManagementClientCapabilitiesCapabilitiesObject

**Framework**: Device Management  
**Kind**: dictionary

A collection of the device’s supported features, payloads, and versions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusManagementClientCapabilitiesCapabilitiesObject
```

## Topics

### Objects
- [object StatusManagementClientCapabilitiesCapabilities_SupportedFeaturesObject](statusmanagementclientcapabilitiescapabilities_supportedfeaturesobject.md)
  A set of optional protocol features that the client supports.
- [object StatusManagementClientCapabilitiesCapabilities_SupportedPayloadsObject](statusmanagementclientcapabilitiescapabilities_supportedpayloadsobject.md)
  The set of declaration and status items that the client supports.

## Properties

- `supported-features` (StatusManagementClientCapabilitiesCapabilities_SupportedFeaturesObject) *(required)*: A set of optional protocol features that the client supports. Each object’s key represents a feature, and the property value represents the feature’s associated parameters.
- `supported-payloads` (StatusManagementClientCapabilitiesCapabilities_SupportedPayloadsObject) *(required)*: A set of declaration and status items that the client supports.
- `supported-versions` ([string]) *(required)*: A list of protocol versions that the client supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmanagementclientcapabilitiescapabilitiesobject)*