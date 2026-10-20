# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that animates the entire value from the root of the key path.

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
init(@KeyframeTrackContentBuilder<Root> content: () -> Content) where Root == Value
```

## Parameters

- `content`: A keyframe collection builder closure containing the keyframes that control the interpolation curve.

## See Also

### Creating a keyframe track
- [init(WritableKeyPath<Root, Value>, content: () -> Content)](./init%28_,content%29.md)
  Creates an instance that animates the property of the root value at the given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframetrack/init(content:))*