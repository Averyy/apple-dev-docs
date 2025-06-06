# Tip.Action

**Framework**: TipKit  
**Kind**: typealias

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
typealias Action = Tips.Action
```

#### Overview

Use actions to provide additional help and guidance for people looking to get started with your tip. Actions appear at the bottom of your [`TipView`](tipview.md) in the form of buttons.

You create an action by providing an `id` and a `title`. The `id` is a string that uniquely identifies the action. The `title` is text that displays as the label on the button.

You can pass a function for the system to call when the action triggers by setting the `perform` attribute in the [`init(id:title:perform:)`](tips/action/init(id:title:perform:).md) initializer. Or you can set the action parameter in the [`init(_:arrowEdge:action:)`](tipview/init(_:arrowedge:action:)-ztv8.md) initializer of your [`TipView`](tipview.md).

## Topics

### Initializers
- [init(id: String?, perform: () -> Void, () -> Text)](tips/action/init(id:perform:_:).md)
  Creates a tip action that displays a custom label.
- [init(id: String?, title: some StringProtocol, perform: () -> Void)](tips/action/init(id:title:perform:).md)
  Creates a tip action that generates its label from a string.

## See Also

- [var actions: [Self.Action]](tip/actions.md)
  Buttons that help people get started or learn more about your feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/action)*