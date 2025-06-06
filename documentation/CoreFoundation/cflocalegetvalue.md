# CFLocaleGetValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the corresponding value for the given key of a locale’s key-value pair.

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
func CFLocaleGetValue(_ locale: CFLocale!, _ key: CFLocaleKey!) -> CFTypeRef!
```

#### Return Value

The value corresponding to the given key in locale. The value may be any type of CFType object. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

Locale objects use key-value pairs to store property values. Use this function to get the value of a specific property.

## Parameters

- `locale`: The locale object to examine.
- `key`: The key for which to obtain the corresponding value. Possible values are described in  .

## See Also

- [func CFLocaleCopyDisplayNameForPropertyValue(CFLocale!, CFLocaleKey!, CFString!) -> CFString!](cflocalecopydisplaynameforpropertyvalue(_:_:_:).md)
  Returns the display name for the given value.
- [func CFLocaleGetIdentifier(CFLocale!) -> CFLocaleIdentifier!](cflocalegetidentifier(_:).md)
  Returns the given locale’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalegetvalue(_:_:))*