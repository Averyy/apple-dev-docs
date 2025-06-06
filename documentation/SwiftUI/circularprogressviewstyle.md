# CircularProgressViewStyle

**Framework**: SwiftUI  
**Kind**: struct

A progress view that uses a circular gauge to indicate the partial completion of an activity.

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
struct CircularProgressViewStyle
```

#### Overview

On watchOS, and in widgets and complications, a circular progress view appears as a gauge with the [`accessoryCircularCapacity`](gaugestyle/accessorycircularcapacity.md) style. If the progress view is indeterminate, the gauge is empty.

In cases where no determinate circular progress view style is available, circular progress views use an indeterminate style.

Use [`circular`](progressviewstyle/circular.md) to construct the circular progress view style.

## Topics

### Creating the progress view style
- [init()](circularprogressviewstyle/init.md)
  Creates a circular progress view style.
### Deprecated initializers
- [init(tint: Color)](circularprogressviewstyle/init(tint:).md)
  Creates a circular progress view style with a tint color.

## Relationships

### Conforms To
- [ProgressViewStyle](progressviewstyle.md)

## See Also

- [struct DefaultProgressViewStyle](defaultprogressviewstyle.md)
  The default progress view style in the current context of the view being styled.
- [struct LinearProgressViewStyle](linearprogressviewstyle.md)
  A progress view that visually indicates its progress using a horizontal bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/circularprogressviewstyle)*