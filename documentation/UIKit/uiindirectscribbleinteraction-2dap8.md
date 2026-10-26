# UIIndirectScribbleInteraction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
@interface UIIndirectScribbleInteraction : NSObject
```

#### Overview

Use [`UIIndirectScribbleInteraction`](./uiindirectscribbleinteraction-1nfjm.md) if your app has a view that looks to the user like a text input but doesn’t implement [`UITextInput`](./uitextinput.md). It makes the view act as a container of one or more virtual “text input elements”, each of which defines an area the user can write into without having to tap first.

Some example uses of [`UIIndirectScribbleInteraction`](./uiindirectscribbleinteraction-1nfjm.md) include:

- A view that looks like a search or text field that in reality is a button, but when tapped installs a real text field.
- A view that contains multiple virtual text fields which the user can normally tap and type into, but aren’t full blown text fields all the time.

## Topics

### Creating an indirect Scribble interaction
- [- initWithDelegate:](./uiindirectscribbleinteraction-2dap8/initwithdelegate_.md)
  Creates an indirect Scribble interaction item with the specified delegate.
### Managing indirect Scribble interactions
- [delegate](./uiindirectscribbleinteraction-2dap8/delegate.md)
  The delegate for the interaction, to supply and customize writable elements in the interaction’s view.
### Detecting writing
- [handlingWriting](./uiindirectscribbleinteraction-2dap8/handlingwriting.md)
  A Boolean value that indicates whether the user is actively writing.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [UIInteraction](./uiinteraction.md)

## See Also

### Custom views
- [UIIndirectScribbleInteractionDelegate](./uiindirectscribbleinteractiondelegate-3jmnk.md)
  Methods that customize behavior on views that aren’t formally text input views.
- [UIScribbleElementIdentifier](./uiscribbleelementidentifier.md)
  The element’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction-2dap8)*