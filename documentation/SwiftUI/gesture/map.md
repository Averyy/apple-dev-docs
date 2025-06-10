# map(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a gesture that uses the given closure to map over this gesture’s value.

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
func map<T>(_ body: @escaping (Self.Value) -> T) -> _MapGesture<Self, T>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/map(_:))*