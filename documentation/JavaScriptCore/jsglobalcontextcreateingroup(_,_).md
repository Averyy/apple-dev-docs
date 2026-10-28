# JSGlobalContextCreateInGroup(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

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

```c
JSGlobalContextRefJSGlobalContextCreateInGroup(JSContextGroupRef group, JSClassRef globalObjectClass);
```

## Return Value

A [`JSGlobalContextRef`](./jsglobalcontextref.md) with a global object of class `globalObjectClass` and a context group equal to `group`.

## Discussion

[`JSGlobalContextCreateInGroup(_:_:)`](./jsglobalcontextcreateingroup%28_,_%29.md) allocates a global object and populates it with all the built-in JavaScript objects, such as `Object`, `Function`, `String`, and `Array`.

## Parameters

- `group`: The context group to use. The created global context retains the group. Pass `NULL` to create a unique group for the context.
- `globalObjectClass`: The class to use when creating the global object. Pass `NULL` to use the default object class.

## See Also

### Creating a global context
- [func JSGlobalContextCreate(JSClassRef!) -> JSGlobalContextRef!](./jsglobalcontextcreate%28_%29.md)
  Creates a global JavaScript execution context.
- [func JSGlobalContextRetain(JSGlobalContextRef!) -> JSGlobalContextRef!](./jsglobalcontextretain%28_%29.md)
  Retains a global JavaScript execution context.
- [func JSGlobalContextRelease(JSGlobalContextRef!)](./jsglobalcontextrelease%28_%29.md)
  Releases a global JavaScript execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextcreateingroup(_:_:))*