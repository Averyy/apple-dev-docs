# accessibilityZoomAction(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityZoomAction(_ handler: @escaping (AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

For example, this is how a zoom action is used to transform the scale of a shape which has a `MagnificationGesture`.

```swift
var body: some View {
    Circle()
        .scaleEffect(magnifyBy)
        .gesture(magnification)
        .accessibilityLabel("Circle Magnifier")
        .accessibilityZoomAction { action in
            switch action.direction {
            case .zoomIn:
                magnifyBy += 0.5
            case .zoomOut:
                 magnifyBy -= 0.5
            }
        }
}
```

## See Also

### Making gestures accessible
- [func accessibilityActivationPoint(_:)](./accessibilityactivationpoint%28_%29.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(_:isEnabled:)](./accessibilityactivationpoint%28_,isenabled%29.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityDragPoint(_:description:)](./accessibilitydragpoint%28_,description%29.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(_:description:isEnabled:)](./accessibilitydragpoint%28_,description,isenabled%29.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(_:description:)](./accessibilitydroppoint%28_,description%29.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(_:description:isEnabled:)](./accessibilitydroppoint%28_,description,isenabled%29.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibilitydirecttouch%28_,options%29.md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [struct AccessibilityDirectTouchOptions](../accessibilitydirecttouchoptions.md)
  An option set that defines the functionality of a view’s direct touch area.
- [struct AccessibilityZoomGestureAction](../accessibilityzoomgestureaction.md)
  Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityzoomaction(_:))*