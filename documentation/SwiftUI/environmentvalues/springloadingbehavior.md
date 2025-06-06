# springLoadingBehavior

**Framework**: SwiftUI  
**Kind**: property

The behavior of spring loaded interactions for the views associated with this environment.

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
var springLoadingBehavior: SpringLoadingBehavior { get }
```

#### Discussion

Spring loading refers to a view being activated during a drag and drop interaction. On iOS this can occur when pausing briefly on top of a view with dragged content. On macOS this can occur with similar brief pauses or on pressure-sensitive systems by “force clicking” during the drag. This has no effect on tvOS or watchOS.

This is commonly used with views that have a navigation or presentation effect, allowing the destination to be revealed without pausing the drag interaction. For example, a button that reveals a list of folders that a dragged item can be dropped onto.

A value of `enabled` means that a view should support spring loaded interactions if it is able, and `disabled` means it should not. A value of `automatic` means that a view should follow its default behavior, such as a `TabView` automatically allowing spring loading, but a `Picker` with `segmented` style would not.

## See Also

- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](view/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [struct SpringLoadingBehavior](springloadingbehavior.md)
  The options for controlling the spring loading behavior of views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/springloadingbehavior)*