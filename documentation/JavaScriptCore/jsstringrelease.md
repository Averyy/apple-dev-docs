# JSStringRelease(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Releases a JavaScript string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringRelease(_ string: JSStringRef!)
```

## Parameters

- `string`: The   to release.

## See Also

- [func JSStringCreateWithCharacters(UnsafePointer<JSChar>!, Int) -> JSStringRef!](jsstringcreatewithcharacters(_:_:).md)
  Creates a JavaScript string from a buffer of Unicode characters.
- [typealias JSChar](jschar.md)
  A Unicode character.
- [func JSStringCreateWithUTF8CString(UnsafePointer<CChar>!) -> JSStringRef!](jsstringcreatewithutf8cstring(_:).md)
  Creates a JavaScript string from a null-terminated UTF-8 string.
- [func JSStringRetain(JSStringRef!) -> JSStringRef!](jsstringretain(_:).md)
  Retains a JavaScript string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringrelease(_:))*