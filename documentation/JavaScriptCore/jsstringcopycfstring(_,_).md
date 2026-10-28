# JSStringCopyCFString(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Creates a Core Foundation string from a JavaScript string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringCopyCFString(_ alloc: CFAllocator!, _ string: JSStringRef!) -> CFString!
```

```c
CFStringRefJSStringCopyCFString(CFAllocatorRef alloc, JSStringRef string);
```

## Return Value

A [`CFString`](../CoreFoundation/cfstring.md) that contains `string`. Ownership follows [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The `alloc` parameter to pass to `CFStringCreate`.
- `string`: The [`JSStringRef`](./jsstringref.md) to copy into the new [`CFString`](../CoreFoundation/cfstring.md).

## See Also

### Converting to and from Core Foundation Strings
- [func JSStringCreateWithCFString(CFString!) -> JSStringRef!](./jsstringcreatewithcfstring%28_%29.md)
  Creates a JavaScript string from a Core Foundation string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringcopycfstring(_:_:))*