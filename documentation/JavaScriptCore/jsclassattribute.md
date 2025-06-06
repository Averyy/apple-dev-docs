# JSClassAttribute

**Framework**: JavaScriptCore

A JavaScript class attribute.

## Topics

### Constants
- [var kJSClassAttributeNone: Int](kjsclassattributenone.md)
  An attribute that specifies that a class has no special attributes.
- [var kJSClassAttributeNoAutomaticPrototype: Int](kjsclassattributenoautomaticprototype.md)
  An attribute that specifies that a class doesn’t automatically generate a shared prototype for its instance objects.

## See Also

- [func JSClassCreate(UnsafePointer<JSClassDefinition>!) -> JSClassRef!](jsclasscreate(_:).md)
  Creates a JavaScript class.
- [func JSClassRelease(JSClassRef!)](jsclassrelease(_:).md)
  Releases a JavaScript class.
- [func JSClassRetain(JSClassRef!) -> JSClassRef!](jsclassretain(_:).md)
  Retains a JavaScript class.
- [let kJSClassDefinitionEmpty: JSClassDefinition](kjsclassdefinitionempty.md)
  A class definition structure of the current version that contains null pointers and has no attributes.
- [struct JSClassDefinition](jsclassdefinition.md)
  A structure that contains properties and callbacks that define a type of object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassattribute)*