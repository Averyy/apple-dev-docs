# JSClassRelease(_:)

**Framework**: JavaScriptCore  
**Kind**: func

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

## Parameters

- `jsClass`: The   to release.

## See Also

- [func JSClassCreate(UnsafePointer<JSClassDefinition>!) -> JSClassRef!](jsclasscreate(_:).md)
  Creates a JavaScript class.
- [func JSClassRetain(JSClassRef!) -> JSClassRef!](jsclassretain(_:).md)
  Retains a JavaScript class.
- [let kJSClassDefinitionEmpty: JSClassDefinition](kjsclassdefinitionempty.md)
  A class definition structure of the current version that contains null pointers and has no attributes.
- [struct JSClassDefinition](jsclassdefinition.md)
  A structure that contains properties and callbacks that define a type of object.
- [JSClassAttribute](jsclassattribute.md)
  A JavaScript class attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassrelease(_:))*