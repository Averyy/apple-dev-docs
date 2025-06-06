# CFNumberFormatterCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new CFNumberFormatter object, localized to the given locale, which will format numbers to the given style.

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
func CFNumberFormatterCreate(_ allocator: CFAllocator!, _ locale: CFLocale!, _ style: CFNumberFormatterStyle) -> CFNumberFormatter!
```

#### Return Value

A new number formatter, localized to the given locale, which will format numbers using the given style. Returns `NULL` if there was a problem creating the formatter. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `locale`: A locale to use for localization. If  , the function uses the default system locale. Use   to specify the locale of the current user.
- `style`: A number style. See   for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattercreate(_:_:_:))*