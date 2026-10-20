# CFDateFormatterGetAbsoluteTimeFromString(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns an absolute time object representing a given string.

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
func CFDateFormatterGetAbsoluteTimeFromString(_ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ atp: UnsafeMutablePointer<CFAbsoluteTime>!) -> Bool
```

```c
extern Boolean CFDateFormatterGetAbsoluteTimeFromString(CFDateFormatterRef formatter, CFStringRef string, CFRange *rangep, CFAbsoluteTime *atp);
```

#### Return Value

`true` if the string was parsed successfully, otherwise `false`.

## Parameters

- `formatter`: The date formatter object to use to parse `string`.
- `string`: The string that contains the time to be parsed.
- `rangep`: Reference to the range within the string specifying the substring to be parsed. If `NULL`, the whole string is parsed. On return, the range that defines the extent of the parse (may be less than the given range).
- `atp`: An absolute time value, returned by reference, that represents `string`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Parsing Strings
- [func CFDateFormatterCreateDateFromString(CFAllocator!, CFDateFormatter!, CFString!, UnsafeMutablePointer<CFRange>!) -> CFDate!](./cfdateformattercreatedatefromstring%28_,_,_,_%29.md)
  Returns a date object representing a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattergetabsolutetimefromstring(_:_:_:_:))*