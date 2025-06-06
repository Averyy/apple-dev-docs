# JSGlobalContextCreate(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a global JavaScript execution context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGlobalContextCreate(_ globalObjectClass: JSClassRef!) -> JSGlobalContextRef!
```

#### Return Value

A [`JSGlobalContextRef`](jsglobalcontextref.md) with a global object of class `globalObjectClass`.

#### Discussion

[`JSGlobalContextCreate(_:)`](jsglobalcontextcreate(_:).md) allocates a global object and populates it with all the built-in JavaScript objects, such as `Object`, `Function`, `String`, and `Array`.

In WebKit 4 and later, the system creates the context in a unique context group. Therefore, scripts may execute in it concurrently with scripts executing in other contexts. However, you may not use values from the context in other contexts.

## Parameters

- `globalObjectClass`: The class to use when creating the global object. Pass   to use the default object class.

## See Also

- [func JSGlobalContextCreateInGroup(JSContextGroupRef!, JSClassRef!) -> JSGlobalContextRef!](jsglobalcontextcreateingroup(_:_:).md)
  Creates a global JavaScript execution context in the provided context group.
- [func JSGlobalContextRetain(JSGlobalContextRef!) -> JSGlobalContextRef!](jsglobalcontextretain(_:).md)
  Retains a global JavaScript execution context.
- [func JSGlobalContextRelease(JSGlobalContextRef!)](jsglobalcontextrelease(_:).md)
  Releases a global JavaScript execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextcreate(_:))*