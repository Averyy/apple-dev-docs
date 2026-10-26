---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier"
framework: "swift-configuration/Configuration"
---

# SecretsSpecifier

**Framework**: swift-configuration/Configuration  
**Kind**: enum  
**Role**: Enumeration

A specification for identifying which configuration values contain sensitive information.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum SecretsSpecifier<KeyType, ValueType> where KeyType : Hashable, KeyType : Sendable, ValueType : Sendable
```

## Mentions

- [Adopting best practices](./best-practices.md)
- [Handling secrets correctly](./handling-secrets-correctly.md)

#### Overview

Configuration providers use secrets specifiers to determine which values should be marked as sensitive and protected from accidental disclosure in logs, debug output, or access reports. Secret values are handled specially by [`AccessReporter`](./accessreporter.md) instances and other components that process configuration data.

#### Usage patterns

##### Mark all values as secret

Use this for providers that exclusively handle sensitive data:

```swift
let provider = InMemoryProvider(
    values: ["api.key": "secret123", "db.password": "pass456"],
    secretsSpecifier: .all
)
```

##### Mark specific keys as secret

Use this when you know which specific keys contain sensitive information:

```swift
let provider = EnvironmentVariablesProvider(
    secretsSpecifier: .specific(
        ["API_KEY", "DATABASE_PASSWORD", "JWT_SECRET"]
    )
)
```

##### Dynamic secret detection

Use this for complex logic that determines secrecy based on key patterns or values:

```swift
let provider = FileProvider<JSONSnapshot>(
    filePath: "/etc/config.json",
    secretsSpecifier: .dynamic { key, value in
        // Mark keys containing "password",
        // "secret", or "token" as secret
        key.lowercased().contains("password") ||
        key.lowercased().contains("secret") ||
        key.lowercased().contains("token")
    }
)
```

##### No secret values

Use this for providers that handle only non-sensitive configuration:

```swift
let provider = InMemoryProvider(
    values: ["app.name": "MyApp", "log.level": "info"],
    secretsSpecifier: .none
)
```

## Topics

### Types of specifiers
- [SecretsSpecifier.all](./secretsspecifier/all.md)
  The library treats all configuration values as secrets.
- [SecretsSpecifier.specific(_:)](./secretsspecifier/specific%28_%29.md)
  The library treats the specified keys as secrets.
- [case dynamic((KeyType, ValueType) -> Bool)](./secretsspecifier/dynamic%28_%29.md)
  The library determines the secret status dynamically by evaluating each key-value pair.
- [SecretsSpecifier.none](./secretsspecifier/none.md)
  The library treats no configuration values as secrets.
### Inspecting a secrets specifier
- [func isSecret(key: KeyType, value: ValueType) -> Bool](./secretsspecifier/issecret%28key,value%29.md)
  Determines whether a configuration value should be treated as secret.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Creating a custom provider
- [Implementing a custom provider](./implementing-a-provider.md)
  Create a custom configuration provider to integrate a new data source.
- [protocol ConfigSnapshot](./configsnapshot.md)
  An immutable snapshot of a configuration provider’s state.
- [protocol FileConfigSnapshot](./fileconfigsnapshot.md)
  A protocol for configuration snapshots created from file data.
- [protocol FileParsingOptions](./fileparsingoptions.md)
  A type that provides parsing options for file configuration snapshots.
- [protocol ConfigProvider](./configprovider.md)
  A type that provides configuration values from a data source.
- [enum ConfigContent](./configcontent.md)
  The raw content of a configuration value.
- [struct ConfigValue](./configvalue.md)
  A configuration value that wraps content with metadata.
- [enum ConfigType](./configtype.md)
  The supported configuration value types.
- [struct LookupResult](./lookupresult.md)
  The result of looking up a configuration value in a provider.
- [struct ConfigUpdatesAsyncSequence](./configupdatesasyncsequence.md)
  A concrete async sequence for delivering updated configuration values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier)*