---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/stringinterpolation"
framework: "swift-log/Logging"
---

# Logger.MetadataValue.StringInterpolation

**Framework**: swift-log/Logging  
**Kind**: struct  
**Role**: Structure

Custom string interpolation that optionally captures metadata attributes.

## Declaration

```swift
struct StringInterpolation
```

#### Overview

When no attributes are specified, produces `.string(...)` — identical to the default `DefaultStringInterpolation` behavior. When any interpolation segment specifies attributes (via the `attributes:` parameter), the result is `.stringConvertible(AttributedStringCarrier(...))` carrying both the string and the accumulated attributes.

Attribute packages (like `LoggingAttributes`) can add overloads with domain-specific parameters (e.g. `sensitivity:`) that call through to `appendInterpolation(_:attributes:)`.

## Topics

### Initializers
- [init(literalCapacity: Int, interpolationCount: Int)](./stringinterpolation/init%28literalcapacity,interpolationcount%29.md)
### Instance Methods
- [func appendInterpolation<T>(T)](./stringinterpolation/appendinterpolation%28_%29-121kb.md)
- [func appendInterpolation<T>(T)](./stringinterpolation/appendinterpolation%28_%29-1ch5o.md)
- [func appendInterpolation<T>(T)](./stringinterpolation/appendinterpolation%28_%29-716sw.md)
- [func appendInterpolation<T>(T)](./stringinterpolation/appendinterpolation%28_%29-91mei.md)
- [func appendInterpolation<T>(T, attributes: @Sendable (inout Logger.MetadataValueAttributes) -> Void)](./stringinterpolation/appendinterpolation%28_,attributes%29-1wm76.md)
- [func appendInterpolation<T>(T, attributes: Logger.MetadataValueAttributes)](./stringinterpolation/appendinterpolation%28_,attributes%29-1zg00.md)
- [func appendInterpolation<T>(T, attributes: @Sendable (inout Logger.MetadataValueAttributes) -> Void)](./stringinterpolation/appendinterpolation%28_,attributes%29-2hhi9.md)
- [func appendInterpolation<T>(T, attributes: @Sendable (inout Logger.MetadataValueAttributes) -> Void)](./stringinterpolation/appendinterpolation%28_,attributes%29-3fdba.md)
- [func appendInterpolation<T>(T, attributes: Logger.MetadataValueAttributes)](./stringinterpolation/appendinterpolation%28_,attributes%29-3tfxd.md)
- [func appendInterpolation<T>(T, attributes: @Sendable (inout Logger.MetadataValueAttributes) -> Void)](./stringinterpolation/appendinterpolation%28_,attributes%29-4khcn.md)
- [func appendInterpolation<T>(T, attributes: Logger.MetadataValueAttributes)](./stringinterpolation/appendinterpolation%28_,attributes%29-5jp83.md)
- [func appendInterpolation<T>(T, attributes: Logger.MetadataValueAttributes)](./stringinterpolation/appendinterpolation%28_,attributes%29-7wlaj.md)
- [func appendInterpolation<T>(T?, default: @autoclosure () -> some StringProtocol)](./stringinterpolation/appendinterpolation%28_,default%29-1nl4c.md)
- [func appendInterpolation<T>(T?, default: @autoclosure () -> some StringProtocol)](./stringinterpolation/appendinterpolation%28_,default%29-30zu4.md)
- [func appendInterpolation<T>(T?, default: @autoclosure () -> some StringProtocol)](./stringinterpolation/appendinterpolation%28_,default%29-9mvck.md)
- [func appendInterpolation<T>(T?, default: @autoclosure () -> some StringProtocol)](./stringinterpolation/appendinterpolation%28_,default%29-9zech.md)
- [func appendLiteral(String)](./stringinterpolation/appendliteral%28_%29.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- Swift.StringInterpolationProtocol


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/stringinterpolation)*