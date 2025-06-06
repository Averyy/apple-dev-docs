# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that animates the property of the root value at the given key path.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(_ keyPath: WritableKeyPath<Root, Value>, @KeyframeTrackContentBuilder<Value> content: () -> Content)
```

## Parameters

- `keyPath`: The property to animate.

## See Also

- [init(content: () -> Content)](keyframetrack/init(content:).md)
  Creates an instance that animates the entire value from the root of the key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframetrack/init(_:content:))*