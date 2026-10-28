# CFLocaleCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a copy of a locale.

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
func CFLocaleCreateCopy(_ allocator: CFAllocator!, _ locale: CFLocale!) -> CFLocale!
```

```c
extern CFLocaleRefCFLocaleCreateCopy(CFAllocatorRef allocator, CFLocaleRef locale);
```

## Return Value

A new locale that is a copy of `locale`. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `locale`: The locale object to copy.

## See Also

### Creating a Locale
- [func CFLocaleCopyCurrent() -> CFLocale!](./cflocalecopycurrent%28%29.md)
  Returns a copy of the logical locale for the current user.
- [func CFLocaleCreate(CFAllocator!, CFLocaleIdentifier!) -> CFLocale!](./cflocalecreate%28_,_%29.md)
  Creates a locale for the given arbitrary locale identifier.
- [func CFLocaleGetSystem() -> CFLocale!](./cflocalegetsystem%28%29.md)
  Returns the root, canonical locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecreatecopy(_:_:))*