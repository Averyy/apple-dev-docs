# removeTokenConfiguration(for:)

**Framework**: CryptoTokenKit  
**Kind**: method

Removes a configuration for a token with the token instance identifier you specify.

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
func removeTokenConfiguration(for instanceID: TKToken.InstanceID)
```

#### Discussion

The method does nothing if the token configuration you specify doesn’t exist.

## Parameters

- `instanceID`: The token’s instance identifier.

## See Also

- [func addTokenConfiguration(for: TKToken.InstanceID) -> TKToken.Configuration](tktokendriver/configuration/addtokenconfiguration(for:).md)
  Creates a configuration object for a token with the token instance identifier you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver/configuration/removetokenconfiguration(for:))*