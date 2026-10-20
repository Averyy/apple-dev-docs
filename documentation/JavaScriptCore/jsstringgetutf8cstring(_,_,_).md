# JSStringGetUTF8CString(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Converts a JavaScript string into a null-terminated UTF-8 string, and copies the result into an external byte buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringGetUTF8CString(_ string: JSStringRef!, _ buffer: UnsafeMutablePointer<CChar>!, _ bufferSize: Int) -> Int
```

#### Return Value

The number of bytes the system writes into `buffer` (including the null-terminator byte).

## Parameters

- `string`: The source [`JSStringRef`](jsstringref.md).
- `buffer`: The destination byte buffer to copy a null-terminated UTF-8 representation of `string` into. On return, `buffer` contains a UTF-8 string representation of `string`. If `bufferSize` is too small, `buffer` contains only partial results. If `buffer` isn’t at least `bufferSize` bytes in size, the conversion results in undefined behavior.
- `bufferSize`: The size of the external buffer in bytes.

## See Also

- [func JSStringGetLength(JSStringRef!) -> Int](jsstringgetlength(_:).md)
  Returns the number of Unicode characters in a JavaScript string.
- [func JSStringGetCharactersPtr(JSStringRef!) -> UnsafePointer<JSChar>!](jsstringgetcharactersptr(_:).md)
  Returns a pointer to the Unicode character buffer that serves as the backing store for a JavaScript string.
- [func JSStringGetMaximumUTF8CStringSize(JSStringRef!) -> Int](jsstringgetmaximumutf8cstringsize(_:).md)
  Returns the maximum number of bytes a JavaScript string uses when you convert it into a null-terminated UTF-8 string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringgetutf8cstring(_:_:_:))*