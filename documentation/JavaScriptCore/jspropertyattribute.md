# JSPropertyAttribute

**Framework**: JavaScriptCore  
**Role**: API Collection

A JavaScript property attribute.

## Topics

### Constants
- [var kJSPropertyAttributeNone: Int](./kjspropertyattributenone.md)
  An attribute that specifies that a property has no special attributes.
- [var kJSPropertyAttributeReadOnly: Int](./kjspropertyattributereadonly.md)
  An attribute that specifies that a property is read-only.
- [var kJSPropertyAttributeDontEnum: Int](./kjspropertyattributedontenum.md)
  An attribute that specifies that property enumerators and JavaScript for-in loops don’t enumerate a property.
- [var kJSPropertyAttributeDontDelete: Int](./kjspropertyattributedontdelete.md)
  An attribute that specifies that the delete operation fails on a property.

## See Also

### Working with Properties
- [func JSPropertyNameAccumulatorAddName(JSPropertyNameAccumulatorRef!, JSStringRef!)](./jspropertynameaccumulatoraddname%28_,_%29.md)
  Adds a property name to a JavaScript property name accumulator.
- [func JSPropertyNameArrayGetCount(JSPropertyNameArrayRef!) -> Int](./jspropertynamearraygetcount%28_%29.md)
  Gets a count of the number of items in a JavaScript property name array.
- [func JSPropertyNameArrayGetNameAtIndex(JSPropertyNameArrayRef!, Int) -> JSStringRef!](./jspropertynamearraygetnameatindex%28_,_%29.md)
  Gets a property name at a specified index in a JavaScript property name array.
- [func JSPropertyNameArrayRelease(JSPropertyNameArrayRef!)](./jspropertynamearrayrelease%28_%29.md)
  Releases a JavaScript property name array.
- [func JSPropertyNameArrayRetain(JSPropertyNameArrayRef!) -> JSPropertyNameArrayRef!](./jspropertynamearrayretain%28_%29.md)
  Retains a JavaScript property name array.
- [typealias JSPropertyAttributes](./jspropertyattributes.md)
  A set of JavaScript property attributes.
- [typealias JSPropertyNameArrayRef](./jspropertynamearrayref.md)
  An array of JavaScript property names.
- [typealias JSPropertyNameAccumulatorRef](./jspropertynameaccumulatorref.md)
  An ordered set of the names of a JavaScript object’s properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jspropertyattribute)*