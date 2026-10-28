# TVTopShelfNamedAttribute

**Framework**: TV Services  
**Kind**: class  
**Role**: Class

An object you use to display additional information.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfNamedAttribute
```

```objc
@interface TVTopShelfNamedAttribute : NSObject
```

## Overview

Use [`TVTopShelfNamedAttribute`](./tvtopshelfnamedattribute.md) objects to specify additional information about your content, such as the names of cast or crew members associated with a movie or show. Each named attribute contains the type of information you want to include (the name) and a list of strings (the values) to display for that attribute. For example, you might set the name property to “Starring” and set the value strings to the names of the leading actors.

Create named attributes and assign them to the [`namedAttributes`](./tvtopshelfcarouselitem/namedattributes.md) property of a [`TVTopShelfCarouselItem`](./tvtopshelfcarouselitem.md) object.

## Topics

### Creating a Named Attribute
- [init(name: String, values: [String])](./tvtopshelfnamedattribute/init%28name,values%29.md)
  Creates a new named attribute object with the specified values.
### Getting the Name and Value
- [var name: String](./tvtopshelfnamedattribute/name.md)
  The localized name of the attribute.
- [var values: [String]](./tvtopshelfnamedattribute/values.md)
  The array of values for the attribute.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Adding Custom Attributes
- [var namedAttributes: [TVTopShelfNamedAttribute]](./tvtopshelfcarouselitem/namedattributes.md)
  Additional information to display for your content, such as a list of leading actors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfnamedattribute)*