# JSValueUnprotect(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Unprotects a JavaScript value from garbage collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueUnprotect(_ ctx: JSContextRef!, _ value: JSValueRef!)
```

#### Discussion

You can protect a value multiple times and must unprotect it an equal number of times before it becomes eligible for garbage collection.

## Parameters

- `ctx`: The execution context to use.
- `value`: The   to unprotect.

## See Also

- [func JSValueProtect(JSContextRef!, JSValueRef!)](jsvalueprotect(_:_:).md)
  Protects a JavaScript value from garbage collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueunprotect(_:_:))*