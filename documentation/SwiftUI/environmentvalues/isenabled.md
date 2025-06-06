# isEnabled

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether the view associated with this environment allows user interaction.

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
var isEnabled: Bool { get set }
```

#### Discussion

The default value is `true`.

## See Also

- [func disabled(Bool) -> some View](view/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [func interactionActivityTrackingTag(String) -> some View](view/interactionactivitytrackingtag(_:).md)
  Sets a tag that you use for tracking interactivity.
- [func invalidatableContent(Bool) -> some View](view/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/isenabled)*