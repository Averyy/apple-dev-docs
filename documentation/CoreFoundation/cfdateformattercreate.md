# CFDateFormatterCreate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new CFDateFormatter object, localized to the given locale, which will format dates to the given date and time styles.

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
func CFDateFormatterCreate(_ allocator: CFAllocator!, _ locale: CFLocale!, _ dateStyle: CFDateFormatterStyle, _ timeStyle: CFDateFormatterStyle) -> CFDateFormatter!
```

#### Return Value

A new date formatter, localized to the given locale, which will format dates to the given date and time styles. Returns `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

You can use `kCFDateFormatterNoStyle` to suppress output for the date or time. The following code fragment illustrates the creation and use of a date formatter that only outputs the date information (memory management is omitted for clarity).

```objc
CFLocaleRef locale = CFLocaleCreate(kCFAllocatorDefault, CFSTR("en_GB"));
 
CFDateFormatterRef formatter = CFDateFormatterCreate(
        kCFAllocatorDefault, locale, kCFDateFormatterMediumStyle, kCFDateFormatterNoStyle);
 
CFDateRef date = CFDateCreate(kCFAllocatorDefault, 123456);
CFStringRef dateAsString = CFDateFormatterCreateStringWithDate (
        kCFAllocatorDefault, formatter, date);
 
CFShow(dateAsString);
// outputs "2 Jan 2001"
```

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `locale`: The locale to use for localization. If   uses the default system local. Use   to specify the locale of the current user.
- `dateStyle`: The date style to use when formatting dates. See   for possible values.
- `timeStyle`: The time style to use when formatting times. See   for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattercreate(_:_:_:_:))*