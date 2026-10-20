# JSStringGetCharactersPtr(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Returns a pointer to the Unicode character buffer that serves as the backing store for a JavaScript string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringGetCharactersPtr(_ string: JSStringRef!) -> UnsafePointer<JSChar>!
```

```c
const JSChar *JSStringGetCharactersPtr(JSStringRef string);
```

#### Return Value

A pointer to the Unicode character buffer that serves as the backing store of `string`, which the system deallocates when it deallocates `string`.

## Parameters

- `string`: The [`JSStringRef`](./jsstringref.md) with the backing store you want to access.

## See Also

### Accessing JavaScript String Information
- [func JSStringGetLength(JSStringRef!) -> Int](./jsstringgetlength%28_%29.md)
  Returns the number of Unicode characters in a JavaScript string.
- [func JSStringGetMaximumUTF8CStringSize(JSStringRef!) -> Int](./jsstringgetmaximumutf8cstringsize%28_%29.md)
  Returns the maximum number of bytes a JavaScript string uses when you convert it into a null-terminated UTF-8 string.
- [func JSStringGetUTF8CString(JSStringRef!, UnsafeMutablePointer<CChar>!, Int) -> Int](./jsstringgetutf8cstring%28_,_,_%29.md)
  Converts a JavaScript string into a null-terminated UTF-8 string, and copies the result into an external byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringgetcharactersptr(_:))*