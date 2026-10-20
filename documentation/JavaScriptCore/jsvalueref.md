# JSValueRef

**Framework**: JavaScriptCore  
**Kind**: typealias  
**Role**: Type Alias

A JavaScript value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSValueRef = OpaquePointer
```

```c
typedef const struct OpaqueJSValue * JSValueRef;
```

#### Discussion

This is the base type for all JavaScript values, and polymorphic functions on them.

## Topics

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
- [struct JSType](./jstype.md)
  Constants that identify the type of a JavaScript value.
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
- [func JSValueMakeSymbol(JSContextRef!, JSStringRef!) -> JSValueRef!](./jsvaluemakesymbol%28_,_%29.md)
  Creates a JavaScript value of the symbol type.
### Converting to Primitive Values
- [func JSValueToBoolean(JSContextRef!, JSValueRef!) -> Bool](./jsvaluetoboolean%28_,_%29.md)
  Converts a JavaScript value to a Boolean and returns the resulting Boolean.
- [func JSValueToNumber(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Double](./jsvaluetonumber%28_,_,_%29.md)
  Converts a JavaScript value to a number and returns the resulting number.
- [func JSValueToStringCopy(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](./jsvaluetostringcopy%28_,_,_%29.md)
  Converts a JavaScript value to a string and copies the result into a JavaScript string.
- [func JSValueToObject(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsvaluetoobject%28_,_,_%29.md)
  Converts a JavaScript value to an object and returns the resulting object.
### Converting to and from JSON-Formatted Strings
- [func JSValueMakeFromJSONString(JSContextRef!, JSStringRef!) -> JSValueRef!](./jsvaluemakefromjsonstring%28_,_%29.md)
  Creates a JavaScript value from a JSON-formatted string.
- [func JSValueCreateJSONString(JSContextRef!, JSValueRef!, UInt32, UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](./jsvaluecreatejsonstring%28_,_,_,_%29.md)
  Creates a JavaScript string that contains the JSON-serialized representation of a JavaScript value.
### Comparing Values
- [func JSValueIsEqual(JSContextRef!, JSValueRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jsvalueisequal%28_,_,_,_%29.md)
  Tests whether two JavaScript values are equal.
- [func JSValueIsStrictEqual(JSContextRef!, JSValueRef!, JSValueRef!) -> Bool](./jsvalueisstrictequal%28_,_,_%29.md)
  Tests whether two JavaScript values are strict equal.
- [func JSValueIsInstanceOfConstructor(JSContextRef!, JSValueRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jsvalueisinstanceofconstructor%28_,_,_,_%29.md)
  Tests whether a JavaScript value is an object that the specified constructor creates.
### Supporting Garbage Collection
- [func JSValueProtect(JSContextRef!, JSValueRef!)](./jsvalueprotect%28_,_%29.md)
  Protects a JavaScript value from garbage collection.
- [func JSValueUnprotect(JSContextRef!, JSValueRef!)](./jsvalueunprotect%28_,_%29.md)
  Unprotects a JavaScript value from garbage collection.

## See Also

### JavaScript Data Types
- [typealias JSObjectRef](./jsobjectref.md)
  A JavaScript object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueref)*