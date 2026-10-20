# JSClassRetain(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Retains a JavaScript class.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSClassRetain(_ jsClass: JSClassRef!) -> JSClassRef!
```

```c
JSClassRefJSClassRetain(JSClassRef jsClass);
```

#### Return Value

A [`JSClassRef`](./jsclassref.md) that is the same as `jsClass`.

## Parameters

- `jsClass`: The [`JSClassRef`](./jsclassref.md) to retain.

## See Also

### Working with Classes
- [func JSClassCreate(UnsafePointer<JSClassDefinition>!) -> JSClassRef!](./jsclasscreate%28_%29.md)
  Creates a JavaScript class.
- [func JSClassRelease(JSClassRef!)](./jsclassrelease%28_%29.md)
  Releases a JavaScript class.
- [let kJSClassDefinitionEmpty: JSClassDefinition](./kjsclassdefinitionempty.md)
  A class definition structure of the current version that contains null pointers and has no attributes.
- [struct JSClassDefinition](./jsclassdefinition.md)
  A structure that contains properties and callbacks that define a type of object.
- [JSClassAttribute](./jsclassattribute.md)
  A JavaScript class attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassretain(_:))*