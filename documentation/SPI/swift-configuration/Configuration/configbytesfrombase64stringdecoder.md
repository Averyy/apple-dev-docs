---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configbytesfrombase64stringdecoder"
framework: "swift-configuration/Configuration"
---

# ConfigBytesFromBase64StringDecoder

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A decoder that converts base64-encoded strings into byte arrays.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfigBytesFromBase64StringDecoder
```

#### Overview

This decoder interprets string configuration values as base64-encoded data and converts them to their binary representation.

## Topics

### Creating bytes from a base64 string
- [init()](./configbytesfrombase64stringdecoder/init%28%29.md)
  Creates a new base64 decoder.
### Default Implementations
- [ConfigBytesFromStringDecoder Implementations](./configbytesfrombase64stringdecoder/configbytesfromstringdecoder-implementations.md)

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
- [struct ConfigBytesFromHexStringDecoder](./configbytesfromhexstringdecoder.md)
  A decoder that converts hexadecimal-encoded strings into byte arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configbytesfrombase64stringdecoder)*