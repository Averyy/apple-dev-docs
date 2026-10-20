# JSType

**Framework**: JavaScriptCore  
**Kind**: struct  
**Role**: Structure

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

```c
typedef enum { ... } JSType;
```

## Topics

### Constants
- [var kJSTypeUndefined: JSType](./kjstypeundefined.md)
  The unique undefined value.
- [var kJSTypeNull: JSType](./kjstypenull.md)
  The unique null value.
- [var kJSTypeBoolean: JSType](./kjstypeboolean.md)
  A primitive Boolean value.
- [var kJSTypeNumber: JSType](./kjstypenumber.md)
  A primitive number value.
- [var kJSTypeString: JSType](./kjstypestring.md)
  A primitive string value.
- [var kJSTypeObject: JSType](./kjstypeobject.md)
  An object value.
- [var kJSTypeSymbol: JSType](./kjstypesymbol.md)
  A primitive symbol value.
### Initializers
- [init(UInt32)](./jstype/init%28_%29.md)
  Creates a JavaScript type.
- [init(rawValue: UInt32)](./jstype/init%28rawvalue%29.md)
  Creates a JavaScript type with the specified raw value.
- [var rawValue: UInt32](./jstype/rawvalue.md)
  The raw value that represents the JavaScript type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

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
- [func JSValueIsNumber(JSContextRef!, JSValueRef!) -> Bool](./jsvalueisnumber%28_,_%29.md)
  Tests whether a JavaScript value’s type is the number type.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jstype)*