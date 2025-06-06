# JSValueMakeNull(_:)

**Framework**: JavaScriptCore  
**Kind**: func

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

#### Return Value

The unique null value.

## Parameters

- `ctx`: The execution context to use.

## See Also

- [func JSValueMakeUndefined(JSContextRef!) -> JSValueRef!](jsvaluemakeundefined(_:).md)
  Creates a JavaScript value of the undefined type.
- [func JSValueMakeBoolean(JSContextRef!, Bool) -> JSValueRef!](jsvaluemakeboolean(_:_:).md)
  Creates a JavaScript Boolean value.
- [func JSValueMakeNumber(JSContextRef!, Double) -> JSValueRef!](jsvaluemakenumber(_:_:).md)
  Creates a JavaScript value of the number type.
- [func JSValueMakeString(JSContextRef!, JSStringRef!) -> JSValueRef!](jsvaluemakestring(_:_:).md)
  Creates a JavaScript value of the string type.
- [func JSValueMakeSymbol(JSContextRef!, JSStringRef!) -> JSValueRef!](jsvaluemakesymbol(_:_:).md)
  Creates a JavaScript value of the symbol type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluemakenull(_:))*