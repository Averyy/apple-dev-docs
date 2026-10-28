# JSStringCreateWithCharacters(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

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

```c
JSStringRefJSStringCreateWithCharacters(const JSChar *chars, size_t numChars);
```

## Return Value

A [`JSStringRef`](./jsstringref.md) that contains `chars`. Ownership follows [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `chars`: The buffer of Unicode characters to copy into the new [`JSStringRef`](./jsstringref.md).
- `numChars`: The number of characters to copy from the buffer that `chars` points to.

## See Also

### Creating a JavaScript String
- [typealias JSChar](./jschar.md)
  A Unicode character.
- [func JSStringCreateWithUTF8CString(UnsafePointer<CChar>!) -> JSStringRef!](./jsstringcreatewithutf8cstring%28_%29.md)
  Creates a JavaScript string from a null-terminated UTF-8 string.
- [func JSStringRetain(JSStringRef!) -> JSStringRef!](./jsstringretain%28_%29.md)
  Retains a JavaScript string.
- [func JSStringRelease(JSStringRef!)](./jsstringrelease%28_%29.md)
  Releases a JavaScript string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringcreatewithcharacters(_:_:))*