# JSObjectMakeArrayBufferWithBytesNoCopy(_:_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript array buffer object from an existing pointer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectMakeArrayBufferWithBytesNoCopy(_ ctx: JSContextRef!, _ bytes: UnsafeMutableRawPointer!, _ byteLength: Int, _ bytesDeallocator: JSTypedArrayBytesDeallocator!, _ deallocatorContext: UnsafeMutableRawPointer!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!
```

#### Return Value

A [`JSObjectRef`](jsobjectref.md) array buffer with a backing store that is the same as the one that `bytes` points to, or `NULL` if there is an error.

#### Discussion

If the system throws an exception during this function, it always calls the `bytesDeallocator`.

## Parameters

- `ctx`: The execution context to use.
- `bytes`: A pointer to the byte buffer to use as the backing store of the typed array object.
- `byteLength`: The number of bytes that   points to.
- `bytesDeallocator`: The allocator to use to deallocate the external buffer when deallocating the typed array object.
- `deallocatorContext`: A pointer to pass back to the deallocator.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSObjectGetArrayBufferByteLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](jsobjectgetarraybufferbytelength(_:_:_:).md)
  Returns the number of bytes in a JavaScript data object.
- [func JSObjectGetArrayBufferBytesPtr(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](jsobjectgetarraybufferbytesptr(_:_:_:).md)
  Returns a pointer to the data buffer that serves as the backing store for a JavaScript typed array object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectmakearraybufferwithbytesnocopy(_:_:_:_:_:_:))*