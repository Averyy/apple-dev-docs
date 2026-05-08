# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance from another gesture.

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
init<T>(_ gesture: T) where Value == T.Value, T : Gesture
```

## Parameters

- `gesture`: A gesture that you use to create a new gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anygesture/init(_:))*