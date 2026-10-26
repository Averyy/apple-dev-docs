---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/jsonsnapshot/parsingoptions/init(bytesdecoder:secretsspecifier:)"
framework: "swift-configuration/Configuration"
---

# init(bytesDecoder:secretsSpecifier:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates parsing options for JSON snapshots.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(bytesDecoder: some ConfigBytesFromStringDecoder = .base64, secretsSpecifier: SecretsSpecifier<String, any Sendable> = .none)
```

## Parameters

- `bytesDecoder`: The decoder to use for converting string values to byte arrays.
- `secretsSpecifier`: The specifier for identifying secret values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/jsonsnapshot/parsingoptions/init(bytesdecoder:secretsspecifier:))*