# JSValueToNumber(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

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

#### Return Value

The numeric result of conversion, or `NaN` if the system throws an exception.

## Parameters

- `ctx`: The execution context to use.
- `value`: The   to convert.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSValueToBoolean(JSContextRef!, JSValueRef!) -> Bool](jsvaluetoboolean(_:_:).md)
  Converts a JavaScript value to a Boolean and returns the resulting Boolean.
- [func JSValueToStringCopy(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](jsvaluetostringcopy(_:_:_:).md)
  Converts a JavaScript value to a string and copies the result into a JavaScript string.
- [func JSValueToObject(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsvaluetoobject(_:_:_:).md)
  Converts a JavaScript value to an object and returns the resulting object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluetonumber(_:_:_:))*