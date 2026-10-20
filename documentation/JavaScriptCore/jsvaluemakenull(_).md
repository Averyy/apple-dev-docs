# JSValueMakeNull(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Creates a JavaScript value of the null type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueMakeNull(_ ctx: JSContextRef!) -> JSValueRef!
```

```c
JSValueRefJSValueMakeNull(JSContextRef ctx);
```

#### Return Value

The unique null value.

## Parameters

- `ctx`: The execution context to use.

## See Also

### Creating Values
- [func JSValueMakeUndefined(JSContextRef!) -> JSValueRef!](./jsvaluemakeundefined%28_%29.md)
  Creates a JavaScript value of the undefined type.
- [func JSValueMakeBoolean(JSContextRef!, Bool) -> JSValueRef!](./jsvaluemakeboolean%28_,_%29.md)
  Creates a JavaScript Boolean value.
- [func JSValueMakeNumber(JSContextRef!, Double) -> JSValueRef!](./jsvaluemakenumber%28_,_%29.md)
  Creates a JavaScript value of the number type.
- [func JSValueMakeString(JSContextRef!, JSStringRef!) -> JSValueRef!](./jsvaluemakestring%28_,_%29.md)
  Creates a JavaScript value of the string type.
- [func JSValueMakeSymbol(JSContextRef!, JSStringRef!) -> JSValueRef!](./jsvaluemakesymbol%28_,_%29.md)
  Creates a JavaScript value of the symbol type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluemakenull(_:))*