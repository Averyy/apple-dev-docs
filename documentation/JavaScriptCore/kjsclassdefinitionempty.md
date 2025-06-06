# kJSClassDefinitionEmpty

**Framework**: JavaScriptCore  
**Kind**: var

A class definition structure of the current version that contains null pointers and has no attributes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kJSClassDefinitionEmpty: JSClassDefinition
```

#### Discussion

Use this constant as a convenience when creating class definitions. For example, to create a class definition with only a finalize method.

```objc
JSClassDefinition definition = kJSClassDefinitionEmpty; 
definition.finalize = Finalize;
```

## See Also

- [func JSClassCreate(UnsafePointer<JSClassDefinition>!) -> JSClassRef!](jsclasscreate(_:).md)
  Creates a JavaScript class.
- [func JSClassRelease(JSClassRef!)](jsclassrelease(_:).md)
  Releases a JavaScript class.
- [func JSClassRetain(JSClassRef!) -> JSClassRef!](jsclassretain(_:).md)
  Retains a JavaScript class.
- [struct JSClassDefinition](jsclassdefinition.md)
  A structure that contains properties and callbacks that define a type of object.
- [JSClassAttribute](jsclassattribute.md)
  A JavaScript class attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/kjsclassdefinitionempty)*