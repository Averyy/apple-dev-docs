---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/environmentvalue(forname:)"
framework: "swift-configuration/Configuration"
---

# environmentValue(forName:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns the raw string value for a specific environment variable name.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func environmentValue(forName name: String) throws -> String?
```

#### Return Value

The string value of the environment variable, or nil if not found.

#### Discussion

This method provides direct access to environment variable values by name, without any key transformation or type conversion. It’s useful when you need to access environment variables that don’t follow the standard configuration key naming conventions.

```swift
let provider = EnvironmentVariablesProvider()
let path = try provider.environmentValue(forName: "PATH")
let home = try provider.environmentValue(forName: "HOME")
```

> **Throws**: Errors accessing environment variable data.

## Parameters

- `name`: The exact name of the environment variable to retrieve.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/environmentvalue(forname:))*