# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create an instance that type-erases `view`.

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
nonisolated
init<V>(_ view: V) where V : View
```

## See Also

### Creating a view
- [init<V>(erasing: V)](./init%28erasing%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anyview/init(_:))*