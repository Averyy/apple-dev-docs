# CFTimeZoneCreateWithTimeIntervalFromGMT(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).

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
func CFTimeZoneCreateWithTimeIntervalFromGMT(_ allocator: CFAllocator!, _ ti: CFTimeInterval) -> CFTimeZone!
```

#### Return Value

A new time zone whose offset from GMT is given by the interval `ti`. The name of the new time zone is GMT +/- the offset, in hours and minutes. Time zones created with this function never have daylight savings, and the offset is constant no matter what the date. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator object to use to allocate memory for the new time zone. Pass   or kCFAllocatorDefault to use the current default allocator.
- `ti`: The offset, from GMT, of the new time zone.

## See Also

- [func CFTimeZoneCreateWithName(CFAllocator!, CFString!, Bool) -> CFTimeZone!](cftimezonecreatewithname(_:_:_:).md)
  Returns the time zone object identified by a given name or abbreviation.
- [func CFTimeZoneCreate(CFAllocator!, CFString!, CFData!) -> CFTimeZone!](cftimezonecreate(_:_:_:).md)
  Creates a time zone with a given name and data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecreatewithtimeintervalfromgmt(_:_:))*