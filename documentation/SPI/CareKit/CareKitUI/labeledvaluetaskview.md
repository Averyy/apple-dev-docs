---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/labeledvaluetaskview"
framework: "CareKit/CareKitUI"
---

# LabeledValueTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

A card that displays a header and a labeled value.

## Declaration

```swift
@MainActor
struct LabeledValueTaskView<Header> where Header : View
```

## Style

The card supports styling using `careKitStyle(_:)`.

```
    +-------------------------------------------------------+
    |                                                       |
    |  <Title>                           <Value>  <Label>   |
    |  <Detail>                                             |
    |                                                       |
    +-------------------------------------------------------+
```

## Topics

### Initializers
- [init(status: LabeledValueTaskViewStatus, header: () -> Header)](./labeledvaluetaskview/init%28status,header%29.md)
  Create an instance.
- [init(title: Text, detail: Text?, status: LabeledValueTaskViewStatus)](./labeledvaluetaskview/init%28title,detail,status%29.md)
  Create an instance with the default header.
### Instance Properties
- [var body: some View](./labeledvaluetaskview/body.md)
### Default Implementations
- [View Implementations](./labeledvaluetaskview/view-implementations.md)
- [View Implementations](./labeledvaluetaskview/view-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- SwiftUICore.View

## See Also

### Read-only care tasks
- [struct NumericProgressTaskView](./numericprogresstaskview.md)
  A card that displays a header, instructions, and indicators for progress and goal values.
- [enum LabeledValueTaskViewStatus](./labeledvaluetaskviewstatus.md)
  The  status denoted by a `LabeledValueTaskView`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/labeledvaluetaskview)*