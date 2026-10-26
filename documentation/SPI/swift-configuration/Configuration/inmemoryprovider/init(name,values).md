---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/inmemoryprovider/init(name:values:)"
framework: "swift-configuration/Configuration"
---

# init(name:values:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new in-memory provider with the specified configuration values.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(name: String? = nil, values: [AbsoluteConfigKey : ConfigValue])
```

#### Discussion

This initializer takes a dictionary of absolute configuration keys mapped to their values. Use this when you have already constructed [`AbsoluteConfigKey`](../absoluteconfigkey.md) instances or when working with keys programmatically.

```swift
let key1 = AbsoluteConfigKey(["database", "host"], context: [:])
let key2 = AbsoluteConfigKey(["database", "port"], context: [:])

let provider = InMemoryProvider(
    name: "database-config",
    values: [
        key1: "localhost",
        key2: 5432
    ]
)
```

## Parameters

- `name`: An optional name for the provider, used in debugging and logging.
- `values`: A dictionary mapping absolute configuration keys to their values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/inmemoryprovider/init(name:values:))*