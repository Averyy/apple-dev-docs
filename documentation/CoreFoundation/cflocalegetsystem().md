# CFLocaleGetSystem()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the root, canonical locale.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFLocaleGetSystem() -> CFLocale!
```

```c
extern CFLocaleRefCFLocaleGetSystem();
```

## Return Value

The root, canonical locale. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

The root locale contains fixed backstop settings for all locale information.

## See Also

### Creating a Locale
- [func CFLocaleCopyCurrent() -> CFLocale!](./cflocalecopycurrent%28%29.md)
  Returns a copy of the logical locale for the current user.
- [func CFLocaleCreate(CFAllocator!, CFLocaleIdentifier!) -> CFLocale!](./cflocalecreate%28_,_%29.md)
  Creates a locale for the given arbitrary locale identifier.
- [func CFLocaleCreateCopy(CFAllocator!, CFLocale!) -> CFLocale!](./cflocalecreatecopy%28_,_%29.md)
  Returns a copy of a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalegetsystem())*