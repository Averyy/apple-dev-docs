---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier/issecret(key:value:)"
framework: "swift-configuration/Configuration"
---

# isSecret(key:value:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Determines whether a configuration value should be treated as secret.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func isSecret(key: KeyType, value: ValueType) -> Bool
```

Available when `KeyType` conforms to `Hashable`, `KeyType` conforms to `Sendable`, and `ValueType` conforms to `Sendable`.

## Return Value

`true` if the value should be treated as secret; otherwise, `false`.

## Discussion

This method evaluates the secrets specifier against the provided key-value pair to determine if the value contains sensitive information that should be protected from disclosure.

```swift
let specifier: SecretsSpecifier<String, String> = .specific(["API_KEY"])
let isSecret = specifier.isSecret(key: "API_KEY", value: "secret123")
// Returns: true
```

## Parameters

- `key`: The provider-specific configuration key.
- `value`: The configuration value to evaluate.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier/issecret(key:value:))*