# TVElementFactory

**Framework**: TVMLKit  
**Kind**: class

An object used to register new elements to extend the Apple TV Markup Language (TVML).

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVElementFactory
```

#### Overview

You must register new elements before initializing a [`TVApplicationController`](tvapplicationcontroller.md) object.

## Topics

### Registering New Elements
- [class func registerViewElementClass(AnyClass, elementName: String)](tvelementfactory/registerviewelementclass(_:elementname:).md)
  Registers a view element for the specified element name.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVImageElement](tvimageelement.md)
  A representation of a read-only DOM node containing the attributes that describe an image element.
- [class TVTextElement](tvtextelement.md)
  The textual content for the DOM element.
- [Creating TVML Elements](creating-tvml-elements.md)
  Avoid rewriting complex and often used elements by creating a simplified custom element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementfactory)*