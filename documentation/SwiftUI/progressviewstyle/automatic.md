# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default progress view style in the current context of the view being styled.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var automatic: DefaultProgressViewStyle { get }
```

Available when `Self` is `DefaultProgressViewStyle`.

#### Discussion

The default style represents the recommended style based on the original initialization parameters of the progress view, and the progress view’s context within the view hierarchy.

## See Also

### Getting built-in progress view styles
- [static var circular: CircularProgressViewStyle](./circular.md)
  The style of a progress view that uses a circular gauge to indicate the partial completion of an activity.
- [static var linear: LinearProgressViewStyle](./linear.md)
  A progress view that visually indicates its progress using a horizontal bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressviewstyle/automatic)*