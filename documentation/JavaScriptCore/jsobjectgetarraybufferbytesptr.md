# JSObjectGetArrayBufferBytesPtr(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Returns a pointer to the data buffer that serves as the backing store for a JavaScript typed array object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectGetArrayBufferBytesPtr(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!
```

#### Discussion

The pointer that this function returns is temporary and may not remain valid across JavaScriptCore API calls.

## Parameters

- `ctx`: The execution context to use.
- `object`: The   with the typed array type data pointer to obtain.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSObjectMakeArrayBufferWithBytesNoCopy(JSContextRef!, UnsafeMutableRawPointer!, Int, JSTypedArrayBytesDeallocator!, UnsafeMutableRawPointer!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakearraybufferwithbytesnocopy(_:_:_:_:_:_:).md)
  Creates a JavaScript array buffer object from an existing pointer.
- [func JSObjectGetArrayBufferByteLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](jsobjectgetarraybufferbytelength(_:_:_:).md)
  Returns the number of bytes in a JavaScript data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectgetarraybufferbytesptr(_:_:_:))*