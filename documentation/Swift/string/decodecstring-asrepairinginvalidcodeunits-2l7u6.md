# decodeCString(_:as:repairingInvalidCodeUnits:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Unknown ?+ - Deprecated
- iOS 8.0+

## Declaration

```swift
static func decodeCString<Encoding>(_ cString: inout Encoding.CodeUnit, as encoding: Encoding.Type, repairingInvalidCodeUnits isRepairing: Bool = true) -> (result: String, repairsMade: Bool)? where Encoding : _UnicodeEncoding
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-2l7u6)*