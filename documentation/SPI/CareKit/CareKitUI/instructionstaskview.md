---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/instructionstaskview"
framework: "CareKit/CareKitUI"
---

# InstructionsTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

A card that displays a header view, multi-line label, and a completion button.

## Declaration

```swift
@MainActor
struct InstructionsTaskView<Header> where Header : View
```

## Overview

In CareKit, this view is intended to display a particular event for a task. The state of the button indicates the completion state of the event.

## Style

The card supports styling using `careKitStyle(_:)`.

```
    +-------------------------------------------------------+
    |                                                       |
    |  <Title>                                              |
    |  <Detail>                                             |
    |                                                       |
    |  --------------------------------------------------   |
    |                                                       |
    |  <Instructions>                                       |
    |                                                       |
    |  +-------------------------------------------------+  |
    |  |               <Completion Button>               |  |
    |  +-------------------------------------------------+  |
    |                                                       |
    +-------------------------------------------------------+
```

## Topics

### Initializers
- [init(instructions: Text?, isComplete: Bool, action: () -> Void, header: () -> Header)](./instructionstaskview/init%28instructions,iscomplete,action,header%29.md)
  Create an instance.
- [init(title: Text, detail: Text?, instructions: Text?, isComplete: Bool, action: () -> Void)](./instructionstaskview/init%28title,detail,instructions,iscomplete,action%29.md)
  Create an instance.
### Instance Properties
- [var body: some View](./instructionstaskview/body.md)
### Default Implementations
- [View Implementations](./instructionstaskview/view-implementations.md)
- [View Implementations](./instructionstaskview/view-implementations.md)

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
- [class OCKInstructionsTaskView](./ockinstructionstaskview.md)
  A card that displays a header, multi-line label, and a completion button.
- [struct CircularCompletionView](./circularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state. The circle will encompass the frame of the provided `content`. To ensure the content is contained within the circle, make sure the content has a square frame.
- [class OCKCheckmarkButton](./ockcheckmarkbutton.md)
  A button that shows a checkmark in the selected state, and an empty ring in the deselected state.
- [struct RectangularCompletionView](./rectangularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/instructionstaskview)*