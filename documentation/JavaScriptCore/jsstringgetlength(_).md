# JSStringGetLength(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Returns the number of Unicode characters in a JavaScript string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringGetLength(_ string: JSStringRef!) -> Int
```

```c
size_t JSStringGetLength(JSStringRef string);
```

## Return Value

The number of Unicode characters in `string`.

## Parameters

- `string`: The [`JSStringRef`](./jsstringref.md) with the length (in Unicode characters) you want to know.

## See Also

### Accessing JavaScript String Information
- [func JSStringGetCharactersPtr(JSStringRef!) -> UnsafePointer<JSChar>!](./jsstringgetcharactersptr%28_%29.md)
  Returns a pointer to the Unicode character buffer that serves as the backing store for a JavaScript string.
- [func JSStringGetMaximumUTF8CStringSize(JSStringRef!) -> Int](./jsstringgetmaximumutf8cstringsize%28_%29.md)
  Returns the maximum number of bytes a JavaScript string uses when you convert it into a null-terminated UTF-8 string.
- [func JSStringGetUTF8CString(JSStringRef!, UnsafeMutablePointer<CChar>!, Int) -> Int](./jsstringgetutf8cstring%28_,_,_%29.md)
  Converts a JavaScript string into a null-terminated UTF-8 string, and copies the result into an external byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringgetlength(_:))*