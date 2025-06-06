# CFLocaleCopyDisplayNameForPropertyValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the display name for the given value.

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
func CFLocaleCopyDisplayNameForPropertyValue(_ displayLocale: CFLocale!, _ key: CFLocaleKey!, _ value: CFString!) -> CFString!
```

#### Return Value

The display name for `value`. Returns `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Note that not all locale property keys have values with display name values.

## Parameters

- `displayLocale`: A locale object.
- `key`: A string that identifies the type that   is. It must be one of the standard locale property keys (see  ).
- `value`: The value for which the display name is required.

## See Also

- [func CFLocaleGetValue(CFLocale!, CFLocaleKey!) -> CFTypeRef!](cflocalegetvalue(_:_:).md)
  Returns the corresponding value for the given key of a locale’s key-value pair.
- [func CFLocaleGetIdentifier(CFLocale!) -> CFLocaleIdentifier!](cflocalegetidentifier(_:).md)
  Returns the given locale’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecopydisplaynameforpropertyvalue(_:_:_:))*