# JSValueIsObjectOfClass(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Tests whether a JavaScript value is an object with a specified class in its class chain.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueIsObjectOfClass(_ ctx: JSContextRef!, _ value: JSValueRef!, _ jsClass: JSClassRef!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `value` is an object and has `jsClass` in its class chain; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `ctx`: The execution context to use.
- `value`: The   to test.
- `jsClass`: The   to test against.

## See Also

- [func JSValueGetType(JSContextRef!, JSValueRef!) -> JSType](jsvaluegettype(_:_:).md)
  Returns a JavaScript value’s type.
- [func JSValueIsUndefined(JSContextRef!, JSValueRef!) -> Bool](jsvalueisundefined(_:_:).md)
  Tests whether a JavaScript value’s type is the undefined type.
- [func JSValueIsNull(JSContextRef!, JSValueRef!) -> Bool](jsvalueisnull(_:_:).md)
  Tests whether a JavaScript value’s type is the null type.
- [func JSValueIsBoolean(JSContextRef!, JSValueRef!) -> Bool](jsvalueisboolean(_:_:).md)
  Tests whether a JavaScript value is Boolean.
- [func JSValueIsNumber(JSContextRef!, JSValueRef!) -> Bool](jsvalueisnumber(_:_:).md)
  Tests whether a JavaScript value’s type is the number type.
- [func JSValueIsString(JSContextRef!, JSValueRef!) -> Bool](jsvalueisstring(_:_:).md)
  Tests whether a JavaScript value’s type is the string type.
- [func JSValueIsSymbol(JSContextRef!, JSValueRef!) -> Bool](jsvalueissymbol(_:_:).md)
  Tests whether a JavaScript value’s type is the symbol type.
- [func JSValueIsObject(JSContextRef!, JSValueRef!) -> Bool](jsvalueisobject(_:_:).md)
  Tests whether a JavaScript value’s type is the object type.
- [func JSValueIsArray(JSContextRef!, JSValueRef!) -> Bool](jsvalueisarray(_:_:).md)
  Tests whether a JavaScript value is an array.
- [func JSValueIsDate(JSContextRef!, JSValueRef!) -> Bool](jsvalueisdate(_:_:).md)
  Tests whether a JavaScript value is a date.
- [func JSValueGetTypedArrayType(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSTypedArrayType](jsvaluegettypedarraytype(_:_:_:).md)
  Returns a JavaScript value’s typed array type.
- [struct JSType](jstype.md)
  Constants that identify the type of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueisobjectofclass(_:_:_:))*