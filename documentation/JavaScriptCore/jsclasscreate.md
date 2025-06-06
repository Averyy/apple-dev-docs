# JSClassCreate(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript class.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSClassCreate(_ definition: UnsafePointer<JSClassDefinition>!) -> JSClassRef!
```

#### Return Value

A [`JSClassRef`](jsclassref.md) with the specified definition suitable for use with [`JSObjectMake(_:_:_:)`](jsobjectmake(_:_:_:).md). Ownership follows [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `definition`: A   that defines the class.

## See Also

- [func JSClassRelease(JSClassRef!)](jsclassrelease(_:).md)
  Releases a JavaScript class.
- [func JSClassRetain(JSClassRef!) -> JSClassRef!](jsclassretain(_:).md)
  Retains a JavaScript class.
- [let kJSClassDefinitionEmpty: JSClassDefinition](kjsclassdefinitionempty.md)
  A class definition structure of the current version that contains null pointers and has no attributes.
- [struct JSClassDefinition](jsclassdefinition.md)
  A structure that contains properties and callbacks that define a type of object.
- [JSClassAttribute](jsclassattribute.md)
  A JavaScript class attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclasscreate(_:))*