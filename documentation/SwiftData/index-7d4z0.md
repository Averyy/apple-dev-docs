# Index(_:)

**Framework**: SwiftData  
**Kind**: macro

Specifies the indices that the schema should apply for this model.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
@freestanding
(declaration) macro Index<T>(_ indices: Schema.Index<T>.Types<T>...) where T : PersistentModel
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/index(_:)-7d4z0)*