# JSValueMakeSymbol(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Creates a JavaScript value of the symbol type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueMakeSymbol(_ ctx: JSContextRef!, _ description: JSStringRef!) -> JSValueRef!
```

```c
JSValueRefJSValueMakeSymbol(JSContextRef ctx, JSStringRef description);
```

## Return Value

A unique [`JSValueRef`](./jsvalueref.md) of the symbol type with a description that matches `description`.

## Parameters

- `ctx`: The execution context to use.
- `description`: A description of the newly created symbol value.

## See Also

### Creating Values
- [func JSValueMakeUndefined(JSContextRef!) -> JSValueRef!](./jsvaluemakeundefined%28_%29.md)
  Creates a JavaScript value of the undefined type.
- [func JSValueMakeNull(JSContextRef!) -> JSValueRef!](./jsvaluemakenull%28_%29.md)
  Creates a JavaScript value of the null type.
- [func JSValueMakeBoolean(JSContextRef!, Bool) -> JSValueRef!](./jsvaluemakeboolean%28_,_%29.md)
  Creates a JavaScript Boolean value.
- [func JSValueMakeNumber(JSContextRef!, Double) -> JSValueRef!](./jsvaluemakenumber%28_,_%29.md)
  Creates a JavaScript value of the number type.
- [func JSValueMakeString(JSContextRef!, JSStringRef!) -> JSValueRef!](./jsvaluemakestring%28_,_%29.md)
  Creates a JavaScript value of the string type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluemakesymbol(_:_:))*