---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/circularcompletionview"
framework: "CareKit/CareKitUI"
---

# CircularCompletionView

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

A view that denotes a completion state. The style of the view differs based on the completion state. The circle will encompass the frame of the provided `content`. To ensure the content is contained within the circle, make sure the content has a square frame.

## Declaration

```swift
@MainActor
struct CircularCompletionView<Content> where Content : View
```

## Style

The view supports styling using `careKitStyle(_:)`.

```
      *   *   *
   *             *
      <Content>
   *             *
      *   *   *
```

## Topics

### Initializers
- [init(isComplete: Bool, content: () -> Content)](./circularcompletionview/init%28iscomplete,content%29.md)
  Create an instance.
### Instance Properties
- [var body: some View](./circularcompletionview/body.md)
### Default Implementations
- [View Implementations](./circularcompletionview/view-implementations.md)
- [View Implementations](./circularcompletionview/view-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- SwiftUICore.View

## See Also

### Single care tasks
- [struct SimpleTaskView](./simpletaskview.md)
  A card that displays a header view and a completion view. The whole view is tappable.
- [class OCKSimpleTaskView](./ocksimpletaskview.md)
  A card that displays an `OCKHeaderView` and a circular checkmark button `completionButton`. In CareKit, this view is intended to display a particular event for a task. The state of the `completionButton` indicates the completion state of the event.
- [struct InstructionsTaskView](./instructionstaskview.md)
  A card that displays a header view, multi-line label, and a completion button.
- [class OCKInstructionsTaskView](./ockinstructionstaskview.md)
  A card that displays a header, multi-line label, and a completion button.
- [class OCKCheckmarkButton](./ockcheckmarkbutton.md)
  A button that shows a checkmark in the selected state, and an empty ring in the deselected state.
- [struct RectangularCompletionView](./rectangularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/circularcompletionview)*