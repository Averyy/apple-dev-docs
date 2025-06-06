# CFLocaleCreate(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a locale for the given arbitrary locale identifier.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFLocaleCreate(_ allocator: CFAllocator!, _ localeIdentifier: CFLocaleIdentifier!) -> CFLocale!
```

#### Return Value

A new locale that corresponds to the arbitrary locale identifier `localeIdentifier`. Returns `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `localeIdentifier`: A string representation of an arbitrary locale identifier.

## See Also

- [func CFLocaleCopyCurrent() -> CFLocale!](cflocalecopycurrent().md)
  Returns a copy of the logical locale for the current user.
- [func CFLocaleCreateCopy(CFAllocator!, CFLocale!) -> CFLocale!](cflocalecreatecopy(_:_:).md)
  Returns a copy of a locale.
- [func CFLocaleGetSystem() -> CFLocale!](cflocalegetsystem().md)
  Returns the root, canonical locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecreate(_:_:))*