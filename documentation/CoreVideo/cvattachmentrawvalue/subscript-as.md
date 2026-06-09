# subscript(_:as:)

**Framework**: Core Video  
**Kind**: subscript

Get or set value associated with the specified key.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript<Value>(key: String, as type: Value.Type = Value.self) -> Value? where Value : CVAttachmentValueRepresentable { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentrawvalue/subscript(_:as:))*