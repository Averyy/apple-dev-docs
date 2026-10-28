# JSStringRetain(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Retains a JavaScript string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringRetain(_ string: JSStringRef!) -> JSStringRef!
```

```c
JSStringRefJSStringRetain(JSStringRef string);
```

## Return Value

A [`JSStringRef`](./jsstringref.md) that is the same as `string`.

## Parameters

- `string`: The [`JSStringRef`](./jsstringref.md) to retain.

## See Also

### Creating a JavaScript String
- [func JSStringCreateWithCharacters(UnsafePointer<JSChar>!, Int) -> JSStringRef!](./jsstringcreatewithcharacters%28_,_%29.md)
  Creates a JavaScript string from a buffer of Unicode characters.
- [typealias JSChar](./jschar.md)
  A Unicode character.
- [func JSStringCreateWithUTF8CString(UnsafePointer<CChar>!) -> JSStringRef!](./jsstringcreatewithutf8cstring%28_%29.md)
  Creates a JavaScript string from a null-terminated UTF-8 string.
- [func JSStringRelease(JSStringRef!)](./jsstringrelease%28_%29.md)
  Releases a JavaScript string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringretain(_:))*