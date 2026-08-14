# UIIndirectScribbleInteraction

**Framework**: UIKit  
**Kind**: class

An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class UIIndirectScribbleInteraction<Delegate> where Delegate : UIIndirectScribbleInteractionDelegate
```

## Topics

### Creating an indirect Scribble interaction
- [init(delegate: Delegate)](uiindirectscribbleinteraction-1nfjm/init(delegate:).md)
  Creates an indirect Scribble interaction item with the specified delegate.
### Managing indirect Scribble interactions
- [var delegate: Delegate?](uiindirectscribbleinteraction-1nfjm/delegate.md)
  The delegate for the interaction, to supply and customize writable elements in the interaction’s view.
### Detecting writing
- [var isHandlingWriting: Bool](uiindirectscribbleinteraction-1nfjm/ishandlingwriting.md)
  A Boolean value that indicates whether the user is actively writing.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [protocol UIIndirectScribbleInteractionDelegate](uiindirectscribbleinteractiondelegate-hdh.md)
  Methods that customize behavior on views that aren’t formally text input views.
- [associatedtype ElementIdentifier : Hashable = String](uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md)
  A unique identifier for a control that isn’t a text field in a Scribble interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction-1nfjm)*