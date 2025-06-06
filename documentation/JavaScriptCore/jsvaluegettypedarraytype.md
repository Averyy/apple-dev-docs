# JSValueGetTypedArrayType(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Returns a JavaScript value’s typed array type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueGetTypedArrayType(_ ctx: JSContextRef!, _ value: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSTypedArrayType
```

#### Return Value

A value of type [`JSTypedArrayType`](jstypedarraytype.md) that identifies the typed array type of `value`, or [`kJSTypedArrayTypeNone`](kjstypedarraytypenone.md) if `value` isn’t a typed array object.

## Parameters

- `ctx`: The execution context to use.
- `value`: The   with the typed array type to return.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

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
- [func JSValueIsObjectOfClass(JSContextRef!, JSValueRef!, JSClassRef!) -> Bool](jsvalueisobjectofclass(_:_:_:).md)
  Tests whether a JavaScript value is an object with a specified class in its class chain.
- [func JSValueIsArray(JSContextRef!, JSValueRef!) -> Bool](jsvalueisarray(_:_:).md)
  Tests whether a JavaScript value is an array.
- [func JSValueIsDate(JSContextRef!, JSValueRef!) -> Bool](jsvalueisdate(_:_:).md)
  Tests whether a JavaScript value is a date.
- [struct JSType](jstype.md)
  Constants that identify the type of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluegettypedarraytype(_:_:_:))*