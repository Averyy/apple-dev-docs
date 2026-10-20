# JSStringCreateWithCFString(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Creates a JavaScript string from a Core Foundation string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringCreateWithCFString(_ string: CFString!) -> JSStringRef!
```

```c
JSStringRefJSStringCreateWithCFString(CFStringRef string);
```

#### Return Value

A [`JSStringRef`](./jsstringref.md) that contains `string`. Ownership follows [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The system optimizes this function to take advantage of cases when [`CFStringGetCharactersPtr(_:)`](../CoreFoundation/cfstringgetcharactersptr%28_%29.md) returns a valid pointer.

## Parameters

- `string`: The [`CFString`](../CoreFoundation/cfstring.md) to copy into the new [`JSStringRef`](./jsstringref.md).

## See Also

### Converting to and from Core Foundation Strings
- [func JSStringCopyCFString(CFAllocator!, JSStringRef!) -> CFString!](./jsstringcopycfstring%28_,_%29.md)
  Creates a Core Foundation string from a JavaScript string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringcreatewithcfstring(_:))*