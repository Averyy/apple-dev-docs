# subscript(_:as:)

**Framework**: SwiftData  
**Kind**: subscript

Returns the model for the specified identifier, downcast to the appropriate class.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
subscript<T>(id: PersistentIdentifier, as as: T.Type) -> T? where T : PersistentModel { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelactor/subscript(_:as:))*