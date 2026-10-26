---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configbytesfromstringdecoder"
framework: "swift-configuration/Configuration"
---

# ConfigBytesFromStringDecoder

**Framework**: swift-configuration/Configuration  
**Kind**: protocol  
**Role**: Protocol

A protocol for decoding string configuration values into byte arrays.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol ConfigBytesFromStringDecoder : Sendable
```

#### Overview

This protocol defines the interface for converting string-based configuration values into binary data. Different implementations can support various encoding formats such as base64, hexadecimal, or other custom encodings.

#### Usage

Implementations of this protocol are used by configuration providers that need to convert string values to binary data, such as cryptographic keys, certificates, or other binary configuration data.

```swift
let decoder: ConfigBytesFromStringDecoder = .base64
let bytes = decoder.decode("SGVsbG8gV29ybGQ=") // "Hello World" in base64
```

## Topics

### Required methods
- [func decode(String) -> [UInt8]?](./configbytesfromstringdecoder/decode%28_%29.md)
  Decodes a string value into an array of bytes.
### Built-in decoders
- [static var base64: ConfigBytesFromBase64StringDecoder](./configbytesfromstringdecoder/base64.md)
  A decoder that interprets string values as base64-encoded data.
- [static var hex: ConfigBytesFromHexStringDecoder](./configbytesfromstringdecoder/hex.md)
  A decoder that interprets string values as hexadecimal-encoded data.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [ConfigBytesFromBase64StringDecoder](./configbytesfrombase64stringdecoder.md)
- [ConfigBytesFromHexStringDecoder](./configbytesfromhexstringdecoder.md)

## See Also

### Value conversion
- [protocol ExpressibleByConfigString](./expressiblebyconfigstring.md)
  A protocol for types that can be initialized from configuration string values.
- [protocol ExpressibleByConfigInt](./expressiblebyconfigint.md)
  A protocol for types that can be initialized from configuration integer values.
- [struct ConfigBytesFromBase64StringDecoder](./configbytesfrombase64stringdecoder.md)
  A decoder that converts base64-encoded strings into byte arrays.
- [struct ConfigBytesFromHexStringDecoder](./configbytesfromhexstringdecoder.md)
  A decoder that converts hexadecimal-encoded strings into byte arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configbytesfromstringdecoder)*