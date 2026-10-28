---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider/init(name:initialvalues:)"
framework: "swift-configuration/Configuration"
---

# init(name:initialValues:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new mutable in-memory provider with the specified initial values.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(name: String? = nil, initialValues: [AbsoluteConfigKey : ConfigValue])
```

## Discussion

This initializer takes a dictionary of absolute configuration keys mapped to their initial values. The provider can be modified after creation using the [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) methods.

```swift
let key1 = AbsoluteConfigKey(["database", "host"], context: [:])
let key2 = AbsoluteConfigKey(["database", "port"], context: [:])

let provider = MutableInMemoryProvider(
    name: "dynamic-config",
    initialValues: [
        key1: "localhost",
        key2: 5432
    ]
)

// Later, update values dynamically
provider.setValue("production-db", forKey: key1)
```

## Parameters

- `name`: An optional name for the provider, used in debugging and logging.
- `initialValues`: A dictionary mapping absolute configuration keys to their initial values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider/init(name:initialvalues:))*