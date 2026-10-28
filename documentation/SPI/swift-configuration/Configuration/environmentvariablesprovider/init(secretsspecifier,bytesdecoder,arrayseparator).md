---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/init(secretsspecifier:bytesdecoder:arrayseparator:)"
framework: "swift-configuration/Configuration"
---

# init(secretsSpecifier:bytesDecoder:arraySeparator:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new provider that reads from the current process environment.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(secretsSpecifier: SecretsSpecifier<String, String> = .none, bytesDecoder: some ConfigBytesFromStringDecoder = .base64, arraySeparator: Character = ",")
```

## Discussion

This initializer creates a provider that reads configuration values from the environment variables of the current process.

```swift
// Basic usage
let provider = EnvironmentVariablesProvider()

// With secret handling
let provider = EnvironmentVariablesProvider(
    secretsSpecifier: .specific(["API_KEY", "DATABASE_PASSWORD"])
)
```

## Parameters

- `secretsSpecifier`: Specifies which environment variables should be treated as secrets.
- `bytesDecoder`: The decoder used for converting string values to byte arrays.
- `arraySeparator`: The character used to separate elements in array values.

## See Also

### Creating an environment variable provider
- [init(environmentVariables: [String : String], secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character)](./init%28environmentvariables,secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider from a custom dictionary of environment variables.
- [init(environmentFilePath: FilePath, allowMissing: Bool, secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character) async throws](./init%28environmentfilepath,allowmissing,secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider that reads from an environment file.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/init(secretsspecifier:bytesdecoder:arrayseparator:))*