# Action

**Framework**: TipKit  
**Kind**: struct  
**Role**: Structure

A type that describes a control associated with a tip.

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
struct Action
```

#### Overview

Use actions to provide additional help and guidance for people looking to get started with your tip. Actions appear at the bottom of your [`TipView`](../tipview.md) in the form of buttons.

You create an action by providing an `id` and a `title`. The `id` is a string that uniquely identifies the action. The `title` is text that displays as the label on the button.

You can pass a function for the system to call when the action triggers by setting the `perform` attribute in the [`init(id:title:perform:)`](./action/init%28id,title,perform%29.md) initializer. Or you can set the action parameter in the [`init(_:arrowEdge:action:)`](../tipview/init%28_,arrowedge,action%29.md) initializer of your [`TipView`](../tipview.md).

## Topics

### Initializers
- [init(id: String?, perform: () -> Void, () -> Text)](./action/init%28id,perform,_%29.md)
  Creates a tip action that displays a custom label.
- [init(id: String?, title: some StringProtocol, perform: () -> Void)](./action/init%28id,title,perform%29.md)
  Creates a tip action that generates its label from a string.
### Instance Properties
- [let handler: () -> Void](./action/handler.md)
- [let id: String](./action/id.md)
  The identifier for a tip’s action.
- [let index: Int?](./action/index.md)
- [let label: () -> Text](./action/label.md)

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/action)*