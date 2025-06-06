# progress

**Framework**: ClassKit  
**Kind**: property

A measure of progress through the task, given as a fraction in the range [0, 1].

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var progress: Double { get set }
```

## Mentions

- [Recording student progress](recording-student-progress.md)

#### Discussion

It’s up to you to define what progress means for each task in your app. For example, you might define progress through a quiz context as the fraction of questions answered. You could report the progress through a video context as a fraction representing the number of minutes watched out of the total minutes in the video.

## See Also

- [func addProgressRange(fromStart: Double, toEnd: Double)](clsactivity/addprogressrange(fromstart:toend:).md)
  Adds a progress range to a given activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/progress)*