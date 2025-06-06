# TVViewElement

**Framework**: TVMLKit  
**Kind**: class

A representation of a read-only DOM node.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVViewElement
```

#### Overview

The `TVViewElement` model object is traversed by the [`TVInterfaceFactory`](tvinterfacefactory.md) factory to construct views and view controllers, and to render templates. Views and view controllers should use the available dispatch APIs to send user events to JavaScript.

## Topics

### Inspecting a View Element
- [var autoHighlightIdentifier: String?](tvviewelement/autohighlightidentifier.md)
  A string identifying the element that is initially in focus.
- [var attributes: [String : String]?](tvviewelement/attributes.md)
  The attributes associated with a view element.
- [var children: [TVViewElement]?](tvviewelement/children.md)
  An array containing the child elements of the element currently being inspected.
- [var isDisabled: Bool](tvviewelement/isdisabled.md)
  Boolean value indicating whether the current element being inspected is disabled.
- [var identifier: String](tvviewelement/identifier.md)
  A string containing the unique identifier for an element.
- [var name: String](tvviewelement/name.md)
  A string containing the element’s name.
- [var parent: TVViewElement?](tvviewelement/parent.md)
  The parent of the current node.
- [var style: TVViewElementStyle?](tvviewelement/style.md)
  The style applied to an element.
- [var updateType: TVElementUpdateType](tvviewelement/updatetype.md)
  The value that describes any changes to the DOM tree after it has been reparsed.
- [enum TVElementUpdateType](tvelementupdatetype.md)
  Describes any changes to the DOM tree after it has been reparsed.
### Dispatching Events
- [func dispatchEvent(type: TVElementEventType, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ((Bool, Bool) -> Void)?)](tvviewelement/dispatchevent(type:canbubble:cancellable:extrainfo:completion:).md)
  Dispatches an event of a specific type to the JavaScript file.
- [enum TVElementEventType](tvelementeventtype.md)
  The type of event that has been dispatched.
- [func dispatchEvent(name: String, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ((Bool, Bool) -> Void)?)](tvviewelement/dispatchevent(name:canbubble:cancellable:extrainfo:completion:).md)
  Dispatches a custom-named event.
### Resetting a Property’s Value
- [func resetProperty(TVElementResettableProperty)](tvviewelement/resetproperty(_:).md)
  Resets the property to its default value.
- [enum TVElementResettableProperty](tvelementresettableproperty.md)
  The types of properties that can be reset to their default values.
### Instance Properties
- [var elementData: [String : Any]](tvviewelement/elementdata.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [TVImageElement](tvimageelement.md)
- [TVTextElement](tvtextelement.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol TVInterfaceCreating](tvinterfacecreating.md)
  A protocol that defines methods used to create views and view controllers.
- [class TVInterfaceFactory](tvinterfacefactory.md)
  A factory for the creation of views and view controllers.
- [class TVBrowserViewController](tvbrowserviewcontroller.md)
  A view controller that presents content in a browsable, full-screen format.
- [class TVDocumentViewController](tvdocumentviewcontroller.md)
  A view controller that represents a TVMLKit document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelement)*