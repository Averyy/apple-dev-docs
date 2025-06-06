# addProgressRange(fromStart:toEnd:)

**Framework**: ClassKit  
**Kind**: method

Adds a progress range to a given activity.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func addProgressRange(fromStart start: Double, toEnd end: Double)
```

## Mentions

- [Recording student progress](recording-student-progress.md)

## Parameters

- `start`: The beginning of the new range to add. This should be fractional value between 0 and 1, inclusive.
- `end`: The end of the new range to add. This should be larger than the   value and less than or equal to one.

## See Also

- [var progress: Double](clsactivity/progress.md)
  A measure of progress through the task, given as a fraction in the range [0, 1].


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/addprogressrange(fromstart:toend:))*