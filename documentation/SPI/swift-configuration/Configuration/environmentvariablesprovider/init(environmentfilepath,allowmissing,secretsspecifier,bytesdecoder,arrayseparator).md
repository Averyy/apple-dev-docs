---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/init(environmentfilepath:allowmissing:secretsspecifier:bytesdecoder:arrayseparator:)"
framework: "swift-configuration/Configuration"
---

# init(environmentFilePath:allowMissing:secretsSpecifier:bytesDecoder:arraySeparator:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new provider that reads from an environment file.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(environmentFilePath: FilePath, allowMissing: Bool = false, secretsSpecifier: SecretsSpecifier<String, String> = .none, bytesDecoder: some ConfigBytesFromStringDecoder = .base64, arraySeparator: Character = ",") async throws
```

## Discussion

This initializer loads environment variables from an `.env` file at the specified path. The file should contain key-value pairs in the format `KEY=value`, one per line. Comments (lines starting with `#`) and empty lines are ignored.

```swift
// Load from a .env file
let provider = try await EnvironmentVariablesProvider(
    environmentFilePath: ".env",
    allowMissing: true,
    secretsSpecifier: .specific(["API_KEY"])
)
```

> **Throws**: If the file is malformed, or if missing when allowMissing is `false`.

## Parameters

- `environmentFilePath`: The file system path to the environment file to load.
- `allowMissing`: A flag controlling how the provider handles a missing file.

  - When `false` (the default), if the file is missing or malformed, throws an error.
  - When `true`, if the file is missing, treats it as empty. Malformed files still throw an error.
- `secretsSpecifier`: Specifies which environment variables should be treated as secrets.
- `bytesDecoder`: The decoder used for converting string values to byte arrays.
- `arraySeparator`: The character used to separate elements in array values.

## See Also

### Creating an environment variable provider
- [init(secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character)](./init%28secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider that reads from the current process environment.
- [init(environmentVariables: [String : String], secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character)](./init%28environmentvariables,secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider from a custom dictionary of environment variables.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/init(environmentfilepath:allowmissing:secretsspecifier:bytesdecoder:arrayseparator:))*