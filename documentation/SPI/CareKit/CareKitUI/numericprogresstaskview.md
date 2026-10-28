---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/numericprogresstaskview"
framework: "CareKit/CareKitUI"
---

# NumericProgressTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

A card that displays a header, instructions, and indicators for progress and goal values.

## Declaration

```swift
@MainActor
struct NumericProgressTaskView<Header> where Header : View
```

## Overview

In CareKit, this view is intended to display a particular event for a task.

```
    +-------------------------------------------------------+
    |                                                       |
    |  <Title>                                              |
    |  <Detail>                                             |
    |                                                       |
    |  --------------------------------------------------   |
    |                                                       |
    |        <Progress Value>          <Goal Value>         |
    |        <Progress Label>          <Goal Label>         |
    |                                                       |
    |                                                       |
    |  <Instructions>                                       |
    |                                                       |
    +-------------------------------------------------------+
```

## Topics

### Initializers
- [init(progress: Text, goal: Text, instructions: Text?, isComplete: Bool, header: () -> Header)](./numericprogresstaskview/init%28progress,goal,instructions,iscomplete,header%29.md)
  Create an instance.
- [init(title: Text, detail: Text?, progress: Text, goal: Text, instructions: Text?, isComplete: Bool)](./numericprogresstaskview/init%28title,detail,progress,goal,instructions,iscomplete%29.md)
  Create an instance.
### Instance Properties
- [var body: some View](./numericprogresstaskview/body.md)
### Default Implementations
- [View Implementations](./numericprogresstaskview/view-implementations.md)
- [View Implementations](./numericprogresstaskview/view-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- SwiftUICore.View

## See Also

### Read-only care tasks
- [struct LabeledValueTaskView](./labeledvaluetaskview.md)
  A card that displays a header and a labeled value.
- [enum LabeledValueTaskViewStatus](./labeledvaluetaskviewstatus.md)
  The  status denoted by a `LabeledValueTaskView`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/numericprogresstaskview)*