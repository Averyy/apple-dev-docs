# JSGlobalContextRef

**Framework**: JavaScriptCore  
**Kind**: typealias

A global JavaScript execution context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSGlobalContextRef = OpaquePointer
```

#### Discussion

A [`JSGlobalContextRef`](jsglobalcontextref.md) is a [`JSContextRef`](jscontextref.md).

## Topics

### Creating a global context
- [func JSGlobalContextCreate(JSClassRef!) -> JSGlobalContextRef!](jsglobalcontextcreate(_:).md)
  Creates a global JavaScript execution context.
- [func JSGlobalContextCreateInGroup(JSContextGroupRef!, JSClassRef!) -> JSGlobalContextRef!](jsglobalcontextcreateingroup(_:_:).md)
  Creates a global JavaScript execution context in the provided context group.
- [func JSGlobalContextRetain(JSGlobalContextRef!) -> JSGlobalContextRef!](jsglobalcontextretain(_:).md)
  Retains a global JavaScript execution context.
- [func JSGlobalContextRelease(JSGlobalContextRef!)](jsglobalcontextrelease(_:).md)
  Releases a global JavaScript execution context.
### Managing the context’s name
- [func JSGlobalContextCopyName(JSGlobalContextRef!) -> JSStringRef!](jsglobalcontextcopyname(_:).md)
  Gets a copy of the name of a context.
- [func JSGlobalContextSetName(JSGlobalContextRef!, JSStringRef!)](jsglobalcontextsetname(_:_:).md)
  Sets the remote debugging name for a context.
### Making a context inspectable
- [func JSGlobalContextIsInspectable(JSGlobalContextRef!) -> Bool](jsglobalcontextisinspectable(_:).md)
  Returns a Boolean value that indicates whether the JavaScript context is inspectable.
- [func JSGlobalContextSetInspectable(JSGlobalContextRef!, Bool)](jsglobalcontextsetinspectable(_:_:).md)
  Sets a JavaScript context to be either inspectable or not inspectable.

## See Also

- [typealias JSContextGroupRef](jscontextgroupref.md)
  A group that associates JavaScript contexts with one another.
- [typealias JSContextRef](jscontextref.md)
  A JavaScript execution context.
- [typealias JSStringRef](jsstringref.md)
  A UTF-16 character buffer.
- [typealias JSClassRef](jsclassref.md)
  A JavaScript class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextref)*