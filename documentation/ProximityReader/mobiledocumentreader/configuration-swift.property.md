# configuration

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The configuration of the mobile document reader.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
final var configuration: MobileDocumentReader.Configuration { get async throws }
```

## Discussion

Use the information contained in the configuration to construct as reader token on your server.

> **Throws**: A [`MobileDocumentReaderError`](../mobiledocumentreadererror.md) if an error occurs.

## See Also

### Retrieving the reader configuration
- [MobileDocumentReader.Configuration](./configuration-swift.struct.md)
  A type that represents the configuration of the mobile document reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentreader/configuration-swift.property)*