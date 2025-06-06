# JSStringRef

**Framework**: JavaScriptCore  
**Kind**: typealias

A UTF-16 character buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSStringRef = OpaquePointer
```

#### Discussion

This is the fundamental string representation in JavaScript.

## Topics

### Creating a JavaScript String
- [func JSStringCreateWithCharacters(UnsafePointer<JSChar>!, Int) -> JSStringRef!](jsstringcreatewithcharacters(_:_:).md)
  Creates a JavaScript string from a buffer of Unicode characters.
- [typealias JSChar](jschar.md)
  A Unicode character.
- [func JSStringCreateWithUTF8CString(UnsafePointer<CChar>!) -> JSStringRef!](jsstringcreatewithutf8cstring(_:).md)
  Creates a JavaScript string from a null-terminated UTF-8 string.
- [func JSStringRetain(JSStringRef!) -> JSStringRef!](jsstringretain(_:).md)
  Retains a JavaScript string.
- [func JSStringRelease(JSStringRef!)](jsstringrelease(_:).md)
  Releases a JavaScript string.
### Accessing JavaScript String Information
- [func JSStringGetLength(JSStringRef!) -> Int](jsstringgetlength(_:).md)
  Returns the number of Unicode characters in a JavaScript string.
- [func JSStringGetCharactersPtr(JSStringRef!) -> UnsafePointer<JSChar>!](jsstringgetcharactersptr(_:).md)
  Returns a pointer to the Unicode character buffer that serves as the backing store for a JavaScript string.
- [func JSStringGetMaximumUTF8CStringSize(JSStringRef!) -> Int](jsstringgetmaximumutf8cstringsize(_:).md)
  Returns the maximum number of bytes a JavaScript string uses when you convert it into a null-terminated UTF-8 string.
- [func JSStringGetUTF8CString(JSStringRef!, UnsafeMutablePointer<CChar>!, Int) -> Int](jsstringgetutf8cstring(_:_:_:).md)
  Converts a JavaScript string into a null-terminated UTF-8 string, and copies the result into an external byte buffer.
### Comparing JavaScript Strings
- [func JSStringIsEqual(JSStringRef!, JSStringRef!) -> Bool](jsstringisequal(_:_:).md)
  Tests whether two JavaScript strings match.
- [func JSStringIsEqualToUTF8CString(JSStringRef!, UnsafePointer<CChar>!) -> Bool](jsstringisequaltoutf8cstring(_:_:).md)
  Tests whether a JavaScript string matches a null-terminated UTF-8 string.
### Converting to and from Core Foundation Strings
- [func JSStringCreateWithCFString(CFString!) -> JSStringRef!](jsstringcreatewithcfstring(_:).md)
  Creates a JavaScript string from a Core Foundation string.
- [func JSStringCopyCFString(CFAllocator!, JSStringRef!) -> CFString!](jsstringcopycfstring(_:_:).md)
  Creates a Core Foundation string from a JavaScript string.

## See Also

- [typealias JSContextGroupRef](jscontextgroupref.md)
  A group that associates JavaScript contexts with one another.
- [typealias JSContextRef](jscontextref.md)
  A JavaScript execution context.
- [typealias JSGlobalContextRef](jsglobalcontextref.md)
  A global JavaScript execution context.
- [typealias JSClassRef](jsclassref.md)
  A JavaScript class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringref)*