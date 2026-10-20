# JSClassRelease(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Releases a JavaScript class.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSClassRelease(_ jsClass: JSClassRef!)
```

```c
void JSClassRelease(JSClassRef jsClass);
```

## Parameters

- `jsClass`: The [`JSClassRef`](./jsclassref.md) to release.

## See Also

### Working with Classes
- [func JSClassCreate(UnsafePointer<JSClassDefinition>!) -> JSClassRef!](./jsclasscreate%28_%29.md)
  Creates a JavaScript class.
- [func JSClassRetain(JSClassRef!) -> JSClassRef!](./jsclassretain%28_%29.md)
  Retains a JavaScript class.
- [let kJSClassDefinitionEmpty: JSClassDefinition](./kjsclassdefinitionempty.md)
  A class definition structure of the current version that contains null pointers and has no attributes.
- [struct JSClassDefinition](./jsclassdefinition.md)
  A structure that contains properties and callbacks that define a type of object.
- [JSClassAttribute](./jsclassattribute.md)
  A JavaScript class attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassrelease(_:))*