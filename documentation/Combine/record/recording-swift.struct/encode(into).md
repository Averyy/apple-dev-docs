# encode(into:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func encode(into encoder: any Encoder) throws
```

Available when `Output` conforms to `Decodable`, `Output` conforms to `Encodable`, `Failure` conforms to `Decodable`, `Failure` conforms to `Encodable`, and `Failure` conforms to `Error`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/recording-swift.struct/encode(into:))*