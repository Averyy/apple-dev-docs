---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configbytesfromhexstringdecoder"
framework: "swift-configuration/Configuration"
---

# ConfigBytesFromHexStringDecoder

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A decoder that converts hexadecimal-encoded strings into byte arrays.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfigBytesFromHexStringDecoder
```

## Overview

This decoder interprets string configuration values as hexadecimal-encoded data and converts them to their binary representation. It expects strings to contain only valid hexadecimal characters (0-9, A-F, a-f).

## Hexadecimal format

The decoder expects strings with an even number of characters, where each pair of characters represents one byte. For example, “48656C6C6F” represents the bytes for “Hello”.

## Topics

### Creating bytes from a hex string decoder
- [init()](./configbytesfromhexstringdecoder/init%28%29.md)
  Creates a new hexadecimal decoder.
### Default Implementations
- [ConfigBytesFromStringDecoder Implementations](./configbytesfromhexstringdecoder/configbytesfromstringdecoder-implementations.md)

## Relationships

### Conforms To
- [ConfigBytesFromStringDecoder](./configbytesfromstringdecoder.md)
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Value conversion
- [protocol ExpressibleByConfigString](./expressiblebyconfigstring.md)
  A protocol for types that can be initialized from configuration string values.
- [protocol ExpressibleByConfigInt](./expressiblebyconfigint.md)
  A protocol for types that can be initialized from configuration integer values.
- [protocol ConfigBytesFromStringDecoder](./configbytesfromstringdecoder.md)
  A protocol for decoding string configuration values into byte arrays.
- [struct ConfigBytesFromBase64StringDecoder](./configbytesfrombase64stringdecoder.md)
  A decoder that converts base64-encoded strings into byte arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configbytesfromhexstringdecoder)*