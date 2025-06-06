# JSStringCreateWithCharacters(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript string from a buffer of Unicode characters.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringCreateWithCharacters(_ chars: UnsafePointer<JSChar>!, _ numChars: Int) -> JSStringRef!
```

#### Return Value

A [`JSStringRef`](jsstringref.md) that contains `chars`. Ownership follows [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `chars`: The buffer of Unicode characters to copy into the new  .
- `numChars`: The number of characters to copy from the buffer that   points to.

## See Also

- [typealias JSChar](jschar.md)
  A Unicode character.
- [func JSStringCreateWithUTF8CString(UnsafePointer<CChar>!) -> JSStringRef!](jsstringcreatewithutf8cstring(_:).md)
  Creates a JavaScript string from a null-terminated UTF-8 string.
- [func JSStringRetain(JSStringRef!) -> JSStringRef!](jsstringretain(_:).md)
  Retains a JavaScript string.
- [func JSStringRelease(JSStringRef!)](jsstringrelease(_:).md)
  Releases a JavaScript string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringcreatewithcharacters(_:_:))*