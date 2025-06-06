# JSType

**Framework**: JavaScriptCore  
**Kind**: struct

Constants that identify the type of a JavaScript value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct JSType
```

## Topics

### Constants
- [var kJSTypeUndefined: JSType](kjstypeundefined.md)
  The unique undefined value.
- [var kJSTypeNull: JSType](kjstypenull.md)
  The unique null value.
- [var kJSTypeBoolean: JSType](kjstypeboolean.md)
  A primitive Boolean value.
- [var kJSTypeNumber: JSType](kjstypenumber.md)
  A primitive number value.
- [var kJSTypeString: JSType](kjstypestring.md)
  A primitive string value.
- [var kJSTypeObject: JSType](kjstypeobject.md)
  An object value.
- [var kJSTypeSymbol: JSType](kjstypesymbol.md)
  A primitive symbol value.
### Initializers
- [init(UInt32)](jstype/init(_:).md)
  Creates a JavaScript type.
- [init(rawValue: UInt32)](jstype/init(rawvalue:).md)
  Creates a JavaScript type with the specified raw value.
- [var rawValue: UInt32](jstype/rawvalue.md)
  The raw value that represents the JavaScript type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [func JSValueGetTypedArrayType(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSTypedArrayType](jsvaluegettypedarraytype(_:_:_:).md)
  Returns a JavaScript value’s typed array type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jstype)*