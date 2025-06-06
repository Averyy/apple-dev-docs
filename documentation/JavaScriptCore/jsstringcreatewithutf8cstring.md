# JSStringCreateWithUTF8CString(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript string from a null-terminated UTF-8 string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringCreateWithUTF8CString(_ string: UnsafePointer<CChar>!) -> JSStringRef!
```

#### Return Value

A [`JSStringRef`](jsstringref.md) that contains `string`. Ownership follows [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `string`: The null-terminated UTF-8 string to copy into the new  .

## See Also

- [func JSStringCreateWithCharacters(UnsafePointer<JSChar>!, Int) -> JSStringRef!](jsstringcreatewithcharacters(_:_:).md)
  Creates a JavaScript string from a buffer of Unicode characters.
- [typealias JSChar](jschar.md)
  A Unicode character.
- [func JSStringRetain(JSStringRef!) -> JSStringRef!](jsstringretain(_:).md)
  Retains a JavaScript string.
- [func JSStringRelease(JSStringRef!)](jsstringrelease(_:).md)
  Releases a JavaScript string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringcreatewithutf8cstring(_:))*