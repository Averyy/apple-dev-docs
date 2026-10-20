# decodeCString(_:as:repairingInvalidCodeUnits:)

**Framework**: Swift  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use a copy of the String argument

## Declaration

```swift
static func decodeCString<Encoding>(_ cString: String, as encoding: Encoding.Type, repairingInvalidCodeUnits isRepairing: Bool = true) -> (result: String, repairsMade: Bool)? where Encoding : _UnicodeEncoding
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-9pdmv)*