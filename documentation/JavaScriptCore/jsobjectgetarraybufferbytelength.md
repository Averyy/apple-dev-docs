# JSObjectGetArrayBufferByteLength(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Returns the number of bytes in a JavaScript data object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectGetArrayBufferByteLength(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Int
```

#### Return Value

The number of bytes in the data object.

## Parameters

- `ctx`: The execution context to use.
- `object`: The JavaScript array buffer object with the length in bytes to return.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSObjectMakeArrayBufferWithBytesNoCopy(JSContextRef!, UnsafeMutableRawPointer!, Int, JSTypedArrayBytesDeallocator!, UnsafeMutableRawPointer!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakearraybufferwithbytesnocopy(_:_:_:_:_:_:).md)
  Creates a JavaScript array buffer object from an existing pointer.
- [func JSObjectGetArrayBufferBytesPtr(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](jsobjectgetarraybufferbytesptr(_:_:_:).md)
  Returns a pointer to the data buffer that serves as the backing store for a JavaScript typed array object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectgetarraybufferbytelength(_:_:_:))*