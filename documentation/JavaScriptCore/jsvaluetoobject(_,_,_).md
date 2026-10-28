# JSValueToObject(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Converts a JavaScript value to an object and returns the resulting object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueToObject(_ ctx: JSContextRef!, _ value: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!
```

```c
JSObjectRefJSValueToObject(JSContextRef ctx, JSValueRef value, JSValueRef*exception);
```

## Return Value

The [`JSObjectRef`](./jsobjectref.md) result of conversion, or `NULL` if the system throws an exception.

## Parameters

- `ctx`: The execution context to use.
- `value`: The [`JSValueRef`](./jsvalueref.md) to convert.
- `exception`: A pointer to a [`JSValueRef`](./jsvalueref.md) to store an exception in, if any. Pass `NULL` to discard any exception.

## See Also

### Converting to Primitive Values
- [func JSValueToBoolean(JSContextRef!, JSValueRef!) -> Bool](./jsvaluetoboolean%28_,_%29.md)
  Converts a JavaScript value to a Boolean and returns the resulting Boolean.
- [func JSValueToNumber(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Double](./jsvaluetonumber%28_,_,_%29.md)
  Converts a JavaScript value to a number and returns the resulting number.
- [func JSValueToStringCopy(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](./jsvaluetostringcopy%28_,_,_%29.md)
  Converts a JavaScript value to a string and copies the result into a JavaScript string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluetoobject(_:_:_:))*