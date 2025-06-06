# JSValueToBoolean(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Converts a JavaScript value to a Boolean and returns the resulting Boolean.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueToBoolean(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool
```

#### Return Value

The Boolean result of conversion.

## Parameters

- `ctx`: The execution context to use.
- `value`: The   to convert.

## See Also

- [func JSValueToNumber(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Double](jsvaluetonumber(_:_:_:).md)
  Converts a JavaScript value to a number and returns the resulting number.
- [func JSValueToStringCopy(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](jsvaluetostringcopy(_:_:_:).md)
  Converts a JavaScript value to a string and copies the result into a JavaScript string.
- [func JSValueToObject(JSContextRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsvaluetoobject(_:_:_:).md)
  Converts a JavaScript value to an object and returns the resulting object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluetoboolean(_:_:))*