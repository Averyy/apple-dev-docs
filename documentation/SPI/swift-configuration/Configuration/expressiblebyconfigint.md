---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/expressiblebyconfigint"
framework: "swift-configuration/Configuration"
---

# ExpressibleByConfigInt

**Framework**: swift-configuration/Configuration  
**Kind**: protocol  
**Role**: Protocol

A protocol for types that can be initialized from configuration integer values.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol ExpressibleByConfigInt : CustomStringConvertible
```

## Mentions

- [Choosing reader methods](./choosing-reader-methods.md)

## Overview

Conform your custom types to this protocol to enable automatic conversion when using the `as:` parameter with configuration reader methods such as [`int(forKey:as:isSecret:fileID:line:)`](./configreader/int%28forkey,as,issecret,fileid,line%29-11fn2.md).

> 💡 **Tip**: If your type is an integer-based enum, you don’t need to explicitly conform it to [`ExpressibleByConfigInt`](./expressiblebyconfigint.md), as the same conversions work for types that conform to `RawRepresentable` with an `Int` raw value automatically.

## Custom types

For other custom types, conform to the protocol [`ExpressibleByConfigInt`](./expressiblebyconfigint.md) by providing a failable initializer and the `configInt` property:

```swift
struct MyDuration: ExpressibleByConfigInt {
    let duration: Duration

    var configInt: Int {
        duration.components.0
    }

    init?(configInt: Int) {
        self.duration = .seconds(configInt)
    }
}

// Now you can use it with automatic conversion
let config = ConfigReader(provider: EnvironmentVariablesProvider())
let dbTimeout = config.int(forKey: "database.timeout", as: MyDuration.self)
```

## Topics

### Required methods
- [init?(configInt: Int)](./expressiblebyconfigint/init%28configint%29.md)
  Creates an instance from a configuration integer value.
### The underlying raw integer value.
- [var configInt: Int](./expressiblebyconfigint/configint.md)
  The underlying raw integer value.
### Default Implementations
- [CustomStringConvertible Implementations](./expressiblebyconfigint/customstringconvertible-implementations.md)

## Relationships

### Inherits From
- Swift.CustomStringConvertible
### Conforming Types
- [Duration](./swift/duration.md)

## See Also

### Value conversion
- [protocol ExpressibleByConfigString](./expressiblebyconfigstring.md)
  A protocol for types that can be initialized from configuration string values.
- [protocol ConfigBytesFromStringDecoder](./configbytesfromstringdecoder.md)
  A protocol for decoding string configuration values into byte arrays.
- [struct ConfigBytesFromBase64StringDecoder](./configbytesfrombase64stringdecoder.md)
  A decoder that converts base64-encoded strings into byte arrays.
- [struct ConfigBytesFromHexStringDecoder](./configbytesfromhexstringdecoder.md)
  A decoder that converts hexadecimal-encoded strings into byte arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/expressiblebyconfigint)*