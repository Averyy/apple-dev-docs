---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/init(environmentvariables:secretsspecifier:bytesdecoder:arrayseparator:)"
framework: "swift-configuration/Configuration"
---

# init(environmentVariables:secretsSpecifier:bytesDecoder:arraySeparator:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new provider from a custom dictionary of environment variables.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(environmentVariables: [String : String], secretsSpecifier: SecretsSpecifier<String, String> = .none, bytesDecoder: some ConfigBytesFromStringDecoder = .base64, arraySeparator: Character = ",")
```

#### Discussion

This initializer allows you to provide a custom set of environment variables, which is useful for testing or when you want to override specific values.

```swift
let customEnvironment = [
    "DATABASE_HOST": "localhost",
    "DATABASE_PORT": "5432",
    "API_KEY": "secret-key"
]
let provider = EnvironmentVariablesProvider(
    environmentVariables: customEnvironment,
    secretsSpecifier: .specific(["API_KEY"])
)
```

## Parameters

- `environmentVariables`: A dictionary of environment variable names and values.
- `secretsSpecifier`: Specifies which environment variables should be treated as secrets.
- `bytesDecoder`: The decoder used for converting string values to byte arrays.
- `arraySeparator`: The character used to separate elements in array values.

## See Also

### Creating an environment variable provider
- [init(secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character)](./init%28secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider that reads from the current process environment.
- [init(environmentFilePath: FilePath, allowMissing: Bool, secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character) async throws](./init%28environmentfilepath,allowmissing,secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider that reads from an environment file.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/init(environmentvariables:secretsspecifier:bytesdecoder:arrayseparator:))*