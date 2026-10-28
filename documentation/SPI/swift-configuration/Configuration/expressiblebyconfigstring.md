---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/expressiblebyconfigstring"
framework: "swift-configuration/Configuration"
---

# ExpressibleByConfigString

**Framework**: swift-configuration/Configuration  
**Kind**: protocol  
**Role**: Protocol

A protocol for types that can be initialized from configuration string values.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol ExpressibleByConfigString : CustomStringConvertible
```

## Mentions

- [Choosing reader methods](./choosing-reader-methods.md)

## Overview

Conform your custom types to this protocol to enable automatic conversion when using the `as:` parameter with configuration reader methods such as [`string(forKey:as:isSecret:fileID:line:)`](./configreader/string%28forkey,as,issecret,fileid,line%29-4oust.md).

> 💡 **Tip**: If your type is a string-based enum, you don’t need to explicitly conform it to [`ExpressibleByConfigString`](./expressiblebyconfigstring.md), as the same conversions work for types that conform to `RawRepresentable` with a `String` raw value automatically.

## Custom types

For other custom types, conform to the protocol [`ExpressibleByConfigString`](./expressiblebyconfigstring.md) by providing a failable initializer and the `description` property:

```swift
struct DatabaseURL: ExpressibleByConfigString {
    let url: URL

    init?(configString: String) {
        guard let url = URL(string: configString) else { return nil }
        self.url = url
    }

    var description: String { url.absoluteString }
}

// Now you can use it with automatic conversion
let config = ConfigReader(provider: EnvironmentVariablesProvider())
let dbUrl = config.string(forKey: "database.url", as: DatabaseURL.self)
```

## Built-in conformances

The following Foundation types already conform to [`ExpressibleByConfigString`](./expressiblebyconfigstring.md):

- `SystemPackage.FilePath` - Converts from file paths.
- `Foundation.URL` - Converts from URL strings.
- `Foundation.UUID` - Converts from UUID strings.
- `Foundation.Date` - Converts from ISO8601 date strings.

## Topics

### Required methods
- [init?(configString: String)](./expressiblebyconfigstring/init%28configstring%29.md)
  Creates an instance from a configuration string value.

## Relationships

### Inherits From
- Swift.CustomStringConvertible
### Conforming Types
- [Date](./foundation/date.md)
- [FilePath](./systempackage/filepath.md)
- [URL](./foundation/url.md)
- [UUID](./foundation/uuid.md)

## See Also

### Value conversion
- [protocol ExpressibleByConfigInt](./expressiblebyconfigint.md)
  A protocol for types that can be initialized from configuration integer values.
- [protocol ConfigBytesFromStringDecoder](./configbytesfromstringdecoder.md)
  A protocol for decoding string configuration values into byte arrays.
- [struct ConfigBytesFromBase64StringDecoder](./configbytesfrombase64stringdecoder.md)
  A decoder that converts base64-encoded strings into byte arrays.
- [struct ConfigBytesFromHexStringDecoder](./configbytesfromhexstringdecoder.md)
  A decoder that converts hexadecimal-encoded strings into byte arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/expressiblebyconfigstring)*