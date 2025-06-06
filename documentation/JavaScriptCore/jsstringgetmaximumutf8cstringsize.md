# JSStringGetMaximumUTF8CStringSize(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Returns the maximum number of bytes a JavaScript string uses when you convert it into a null-terminated UTF-8 string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringGetMaximumUTF8CStringSize(_ string: JSStringRef!) -> Int
```

#### Return Value

The maximum number of bytes that might be necessary to convert `string` into a null-terminated UTF-8 string. The number of bytes that the conversion actually ends up requiring can be less than this, but never more.

## Parameters

- `string`: The   with the maximum converted size (in bytes) you want to know.

## See Also

- [func JSStringGetLength(JSStringRef!) -> Int](jsstringgetlength(_:).md)
  Returns the number of Unicode characters in a JavaScript string.
- [func JSStringGetCharactersPtr(JSStringRef!) -> UnsafePointer<JSChar>!](jsstringgetcharactersptr(_:).md)
  Returns a pointer to the Unicode character buffer that serves as the backing store for a JavaScript string.
- [func JSStringGetUTF8CString(JSStringRef!, UnsafeMutablePointer<CChar>!, Int) -> Int](jsstringgetutf8cstring(_:_:_:).md)
  Converts a JavaScript string into a null-terminated UTF-8 string, and copies the result into an external byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringgetmaximumutf8cstringsize(_:))*