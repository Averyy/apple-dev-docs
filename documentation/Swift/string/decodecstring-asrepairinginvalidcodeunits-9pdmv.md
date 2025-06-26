# decodeCString(_:as:repairingInvalidCodeUnits:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Unknown ?+ - Deprecated
- Mac Catalyst 13.0+

## Declaration

```swift
static func decodeCString<Encoding>(_ cString: String, as encoding: Encoding.Type, repairingInvalidCodeUnits isRepairing: Bool = true) -> (result: String, repairsMade: Bool)? where Encoding : _UnicodeEncoding
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-9pdmv)*