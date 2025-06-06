# CFLocaleGetIdentifier(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the given locale’s identifier.

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
func CFLocaleGetIdentifier(_ locale: CFLocale!) -> CFLocaleIdentifier!
```

#### Return Value

A string representation of `locale`’s identifier. This may not be the same string that was used to create the locale—it may be canonicalized. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `locale`: The locale object to examine.

## See Also

- [func CFLocaleCopyDisplayNameForPropertyValue(CFLocale!, CFLocaleKey!, CFString!) -> CFString!](cflocalecopydisplaynameforpropertyvalue(_:_:_:).md)
  Returns the display name for the given value.
- [func CFLocaleGetValue(CFLocale!, CFLocaleKey!) -> CFTypeRef!](cflocalegetvalue(_:_:).md)
  Returns the corresponding value for the given key of a locale’s key-value pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalegetidentifier(_:))*