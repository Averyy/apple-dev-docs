# environment

**Framework**: SwiftUI  
**Kind**: property

The current environment of the view that created the custom animation.

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
var environment: EnvironmentValues { get }
```

#### Discussion

An instance of [`CustomAnimation`](customanimation.md) uses this property to read environment values from the view that created the animation. To learn more about environment values including how to define custom environment values, see [`EnvironmentValues`](environmentvalues.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationcontext/environment)*