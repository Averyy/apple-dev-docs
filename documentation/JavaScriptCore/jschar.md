# JSChar

**Framework**: JavaScriptCore  
**Kind**: typealias  
**Role**: Type Alias

A Unicode character.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSChar = UInt16
```

```c
typedef unsigned short JSChar;
```

## See Also

### Creating a JavaScript String
- [func JSStringCreateWithCharacters(UnsafePointer<JSChar>!, Int) -> JSStringRef!](./jsstringcreatewithcharacters%28_,_%29.md)
  Creates a JavaScript string from a buffer of Unicode characters.
- [func JSStringCreateWithUTF8CString(UnsafePointer<CChar>!) -> JSStringRef!](./jsstringcreatewithutf8cstring%28_%29.md)
  Creates a JavaScript string from a null-terminated UTF-8 string.
- [func JSStringRetain(JSStringRef!) -> JSStringRef!](./jsstringretain%28_%29.md)
  Retains a JavaScript string.
- [func JSStringRelease(JSStringRef!)](./jsstringrelease%28_%29.md)
  Releases a JavaScript string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jschar)*