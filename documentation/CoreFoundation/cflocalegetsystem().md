# CFLocaleGetSystem()

**Framework**: Core Foundation  
**Kind**: func

Returns the root, canonical locale.

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
func CFLocaleGetSystem() -> CFLocale!
```

#### Return Value

The root, canonical locale. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

The root locale contains fixed backstop settings for all locale information.

## See Also

- [func CFLocaleCopyCurrent() -> CFLocale!](cflocalecopycurrent().md)
  Returns a copy of the logical locale for the current user.
- [func CFLocaleCreate(CFAllocator!, CFLocaleIdentifier!) -> CFLocale!](cflocalecreate(_:_:).md)
  Creates a locale for the given arbitrary locale identifier.
- [func CFLocaleCreateCopy(CFAllocator!, CFLocale!) -> CFLocale!](cflocalecreatecopy(_:_:).md)
  Returns a copy of a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalegetsystem())*