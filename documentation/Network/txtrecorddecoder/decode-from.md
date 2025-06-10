# decode(_:from:)

**Framework**: Network  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func decode<T>(_ type: T.Type, from txtRecord: NWTXTRecord) throws -> T where T : Decodable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/txtrecorddecoder/decode(_:from:))*