# JSValueMakeBoolean(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript Boolean value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueMakeBoolean(_ ctx: JSContextRef!, _ boolean: Bool) -> JSValueRef!
```

#### Return Value

A [`JSValueRef`](jsvalueref.md) of the Boolean type that represents the value of `boolean`.

## Parameters

- `ctx`: The execution context to use.
- `boolean`: The Boolean value to assign to the newly created  .

## See Also

- [func JSValueMakeUndefined(JSContextRef!) -> JSValueRef!](jsvaluemakeundefined(_:).md)
  Creates a JavaScript value of the undefined type.
- [func JSValueMakeNull(JSContextRef!) -> JSValueRef!](jsvaluemakenull(_:).md)
  Creates a JavaScript value of the null type.
- [func JSValueMakeNumber(JSContextRef!, Double) -> JSValueRef!](jsvaluemakenumber(_:_:).md)
  Creates a JavaScript value of the number type.
- [func JSValueMakeString(JSContextRef!, JSStringRef!) -> JSValueRef!](jsvaluemakestring(_:_:).md)
  Creates a JavaScript value of the string type.
- [func JSValueMakeSymbol(JSContextRef!, JSStringRef!) -> JSValueRef!](jsvaluemakesymbol(_:_:).md)
  Creates a JavaScript value of the symbol type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluemakeboolean(_:_:))*