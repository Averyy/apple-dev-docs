# JSValueToNumber(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Converts a JavaScript value to a number and returns the resulting number.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueToNumber(_ ctx: JSContextRef!, _ value: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Double
```

```c
double JSValueToNumber(JSContextRef ctx, JSValueRef value, JSValueRef*exception);
```

#### Return Value

The numeric result of conversion, or `NaN` if the system throws an exception.

## Parameters

- `ctx`: The execution context to use.
- `value`: The [`JSValueRef`](./jsvalueref.md) to convert.
- `exception`: A pointer to a [`JSValueRef`](./jsvalueref.md) to store an exception in, if any. Pass `NULL` to discard any exception.

## See Also

### Converting to Primitive Values
- [func JSValueToBoolean(JSContextRef!, JSValueRef!) -> Bool](./jsvaluetoboolean%28_,_%29.md)
  Converts a JavaScript value to a Boolean and returns the resulting Boolean.
- [func JSValueToStringCopy(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](./jsvaluetostringcopy%28_,_,_%29.md)
  Converts a JavaScript value to a string and copies the result into a JavaScript string.
- [func JSValueToObject(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsvaluetoobject%28_,_,_%29.md)
  Converts a JavaScript value to an object and returns the resulting object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluetonumber(_:_:_:))*