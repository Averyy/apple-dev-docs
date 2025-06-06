# addTokenConfiguration(for:)

**Framework**: CryptoTokenKit  
**Kind**: method

Creates a configuration object for a token with the token instance identifier you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func addTokenConfiguration(for instanceID: TKToken.InstanceID) -> TKToken.Configuration
```

#### Return Value

The configuration class for the token.

#### Discussion

This method adds the created configuration into the [`tokenConfigurations`](tktokendriver/configuration/tokenconfigurations.md) dictionary. Adding a configuration with an `instanceID` that already exists replaces the existing configuration with a new empty configuration.

## Parameters

- `instanceID`: The token’s instance identifier.

## See Also

- [func removeTokenConfiguration(for: TKToken.InstanceID)](tktokendriver/configuration/removetokenconfiguration(for:).md)
  Removes a configuration for a token with the token instance identifier you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver/configuration/addtokenconfiguration(for:))*