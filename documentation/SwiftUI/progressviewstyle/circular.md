# circular

**Framework**: SwiftUI  
**Kind**: property

The style of a progress view that uses a circular gauge to indicate the partial completion of an activity.

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
@preconcurrency static var circular: CircularProgressViewStyle { get }
```

#### Discussion

On watchOS, and in widgets and complications, a circular progress view appears as a gauge with the [`accessoryCircularCapacity`](gaugestyle/accessorycircularcapacity.md) style. If the progress view is indeterminate, the gauge is empty.

In cases where no determinate circular progress view style is available, circular progress views use an indeterminate style.

## See Also

- [static var automatic: DefaultProgressViewStyle](progressviewstyle/automatic.md)
  The default progress view style in the current context of the view being styled.
- [static var linear: LinearProgressViewStyle](progressviewstyle/linear.md)
  A progress view that visually indicates its progress using a horizontal bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressviewstyle/circular)*