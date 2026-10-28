# JSValueIsNumber(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Tests whether a JavaScript value’s type is the number type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueIsNumber(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool
```

```c
bool JSValueIsNumber(JSContextRef ctx, JSValueRef value);
```

## Return Value

[`true`](../Swift/true.md) if the type of `value` is the number type; otherwise, [`false`](../Swift/false.md).

## Parameters

- `ctx`: The execution context to use.
- `value`: The [`JSValueRef`](./jsvalueref.md) to test.

## See Also

### Testing the Value’s Type
- [func JSValueGetType(JSContextRef!, JSValueRef!) -> JSType](./jsvaluegettype%28_,_%29.md)
  Returns a JavaScript value’s type.
- [func JSValueIsUndefined(JSContextRef!, JSValueRef!) -> Bool](./jsvalueisundefined%28_,_%29.md)
  Tests whether a JavaScript value’s type is the undefined type.
- [func JSValueIsNull(JSContextRef!, JSValueRef!) -> Bool](./jsvalueisnull%28_,_%29.md)
  Tests whether a JavaScript value’s type is the null type.
- [func JSValueIsBoolean(JSContextRef!, JSValueRef!) -> Bool](./jsvalueisboolean%28_,_%29.md)
  Tests whether a JavaScript value is Boolean.
- [func JSValueIsString(JSContextRef!, JSValueRef!) -> Bool](./jsvalueisstring%28_,_%29.md)
  Tests whether a JavaScript value’s type is the string type.
- [func JSValueIsSymbol(JSContextRef!, JSValueRef!) -> Bool](./jsvalueissymbol%28_,_%29.md)
  Tests whether a JavaScript value’s type is the symbol type.
- [func JSValueIsObject(JSContextRef!, JSValueRef!) -> Bool](./jsvalueisobject%28_,_%29.md)
  Tests whether a JavaScript value’s type is the object type.
- [func JSValueIsObjectOfClass(JSContextRef!, JSValueRef!, JSClassRef!) -> Bool](./jsvalueisobjectofclass%28_,_,_%29.md)
  Tests whether a JavaScript value is an object with a specified class in its class chain.
- [func JSValueIsArray(JSContextRef!, JSValueRef!) -> Bool](./jsvalueisarray%28_,_%29.md)
  Tests whether a JavaScript value is an array.
- [func JSValueIsDate(JSContextRef!, JSValueRef!) -> Bool](./jsvalueisdate%28_,_%29.md)
  Tests whether a JavaScript value is a date.
- [func JSValueGetTypedArrayType(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSTypedArrayType](./jsvaluegettypedarraytype%28_,_,_%29.md)
  Returns a JavaScript value’s typed array type.
- [struct JSType](./jstype.md)
  Constants that identify the type of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueisnumber(_:_:))*