# CFTimeZoneCreateWithName(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the time zone object identified by a given name or abbreviation.

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
func CFTimeZoneCreateWithName(_ allocator: CFAllocator!, _ name: CFString!, _ tryAbbrev: Bool) -> CFTimeZone!
```

```c
extern CFTimeZoneRefCFTimeZoneCreateWithName(CFAllocatorRef allocator, CFStringRef name, Boolean tryAbbrev);
```

#### Return Value

A time zone corresponding to `name`, or `NULL` if no match was found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator object to use to allocate memory for the new time zone. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `name`: The name or abbreviation of the time zone to obtain. The name may be in any of the formats understood by the system, for example “EST”, “Etc/GMT-2”, “America/Argentina/Buenos_Aires”, “Europe/Monaco”, “US/Pacific”, or “posixrules”. For a complete list of system names, you can see the output of  [`CFTimeZoneCopyKnownNames()`](./cftimezonecopyknownnames%28%29.md).
- `tryAbbrev`: If `false`, assumes `name` is not an abbreviation and searches the time zone information directory for a matching name. If `true`, tries to resolve `name` using the abbreviation dictionary first before searching the information dictionary.

## See Also

### Creating a Time Zone
- [func CFTimeZoneCreateWithTimeIntervalFromGMT(CFAllocator!, CFTimeInterval) -> CFTimeZone!](./cftimezonecreatewithtimeintervalfromgmt%28_,_%29.md)
  Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).
- [func CFTimeZoneCreate(CFAllocator!, CFString!, CFData!) -> CFTimeZone!](./cftimezonecreate%28_,_,_%29.md)
  Creates a time zone with a given name and data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecreatewithname(_:_:_:))*