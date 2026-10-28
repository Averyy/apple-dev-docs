# JSValueMakeString(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Creates a JavaScript value of the string type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueMakeString(_ ctx: JSContextRef!, _ string: JSStringRef!) -> JSValueRef!
```

```c
JSValueRefJSValueMakeString(JSContextRef ctx, JSStringRef string);
```

## Return Value

A [`JSValueRef`](./jsvalueref.md) of the string type that represents the value of `string`.

## Parameters

- `ctx`: The execution context to use.
- `string`: The [`JSStringRef`](./jsstringref.md) to assign to the newly created [`JSValueRef`](./jsvalueref.md). The newly created [`JSValueRef`](./jsvalueref.md) retains `string`, and releases it upon garbage collection.

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
- [func JSValueMakeSymbol(JSContextRef!, JSStringRef!) -> JSValueRef!](./jsvaluemakesymbol%28_,_%29.md)
  Creates a JavaScript value of the symbol type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluemakestring(_:_:))*