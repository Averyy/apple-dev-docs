---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/commandlineargumentsprovider/init(arguments:secretsspecifier:bytesdecoder:)"
framework: "swift-configuration/Configuration"
---

# init(arguments:secretsSpecifier:bytesDecoder:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new CLI provider with the provided arguments.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(arguments: [String] = CommandLine.arguments, secretsSpecifier: SecretsSpecifier<String, String> = .none, bytesDecoder: some ConfigBytesFromStringDecoder = .base64)
```

#### Discussion

```swift
// Uses the current process's arguments.
let provider = CommandLineArgumentsProvider()
```

```swift
// Uses custom arguments.
let provider = CommandLineArgumentsProvider(arguments: ["program", "--test", "--port", "8089"])
```

## Parameters

- `arguments`: The command-line arguments to parse.
- `secretsSpecifier`: Specifies which CLI arguments should be treated as secret.
- `bytesDecoder`: The decoder used for converting string values into bytes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/commandlineargumentsprovider/init(arguments:secretsspecifier:bytesdecoder:))*