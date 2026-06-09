# TupleContent

**Framework**: SwiftUI  
**Kind**: struct

Content created from a tuple of content to be treated as siblings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@frozen
struct TupleContent<each Content>
```

#### Overview

You will rarely, if ever, need to create a `TupleContent` directly. Instead, `TupleContent` will be constructed on your behalf when using a `ContentBuilder`.

This type should be conformed to builder DSL protocols to represent tuple content in that DSL.

`TupleContent` defines a `body` property of type `Never` to improve the ergonomics of conforming to multiple DSL protocols, which should all use `Never` as the universal “primitive body” type.

## Topics

### Creating tuple content
- [init(_:)](tuplecontent/init(_:).md)
### Getting tuple content
- [var content: (repeat each Content)](tuplecontent/content.md)

## Relationships

### Conforms To
- [AccessibilityRotorContent](accessibilityrotorcontent.md)
- [ChartContent](../Charts/ChartContent.md)
- [Commands](commands.md)
- [Copyable](../Swift/Copyable.md)
- [CustomizableToolbarContent](customizabletoolbarcontent.md)
- [Escapable](../Swift/Escapable.md)
- [SceneAccessoryContent](sceneaccessorycontent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [ToolbarContent](toolbarcontent.md)
- [View](view.md)

## See Also

- [typealias EmptyContent](emptycontent.md)
  Content which contains nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tuplecontent)*