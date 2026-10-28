# JSValueProtect(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Protects a JavaScript value from garbage collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueProtect(_ ctx: JSContextRef!, _ value: JSValueRef!)
```

```c
void JSValueProtect(JSContextRef ctx, JSValueRef value);
```

## Discussion

Use this method when you want to store a [`JSValueRef`](./jsvalueref.md) in a global or on the heap, where the garbage collector can’t discover your reference to it.

You can protect a value multiple times and must unprotect it an equal number of times before it becomes eligible for garbage collection.

## Parameters

- `ctx`: The execution context to use.
- `value`: The [`JSValueRef`](./jsvalueref.md) to protect.

## See Also

### Supporting Garbage Collection
- [func JSValueUnprotect(JSContextRef!, JSValueRef!)](./jsvalueunprotect%28_,_%29.md)
  Unprotects a JavaScript value from garbage collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueprotect(_:_:))*