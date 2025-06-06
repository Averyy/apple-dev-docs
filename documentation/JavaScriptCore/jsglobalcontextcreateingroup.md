# JSGlobalContextCreateInGroup(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a global JavaScript execution context in the provided context group.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGlobalContextCreateInGroup(_ group: JSContextGroupRef!, _ globalObjectClass: JSClassRef!) -> JSGlobalContextRef!
```

#### Return Value

A [`JSGlobalContextRef`](jsglobalcontextref.md) with a global object of class `globalObjectClass` and a context group equal to `group`.

#### Discussion

[`JSGlobalContextCreateInGroup(_:_:)`](jsglobalcontextcreateingroup(_:_:).md) allocates a global object and populates it with all the built-in JavaScript objects, such as `Object`, `Function`, `String`, and `Array`.

## Parameters

- `group`: The context group to use. The created global context retains the group. Pass   to create a unique group for the context.
- `globalObjectClass`: The class to use when creating the global object. Pass   to use the default object class.

## See Also

- [func JSGlobalContextCreate(JSClassRef!) -> JSGlobalContextRef!](jsglobalcontextcreate(_:).md)
  Creates a global JavaScript execution context.
- [func JSGlobalContextRetain(JSGlobalContextRef!) -> JSGlobalContextRef!](jsglobalcontextretain(_:).md)
  Retains a global JavaScript execution context.
- [func JSGlobalContextRelease(JSGlobalContextRef!)](jsglobalcontextrelease(_:).md)
  Releases a global JavaScript execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextcreateingroup(_:_:))*