# CFTimeZoneCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a time zone with a given name and data.

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
func CFTimeZoneCreate(_ allocator: CFAllocator!, _ name: CFString!, _ data: CFData!) -> CFTimeZone!
```

```c
extern CFTimeZoneRefCFTimeZoneCreate(CFAllocatorRef allocator, CFStringRef name, CFDataRef data);
```

## Return Value

A time zone corresponding to `name` and `data`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You typically do not call this function directly. Use the [`CFTimeZoneCreateWithName(_:_:_:)`](./cftimezonecreatewithname%28_,_,_%29.md) function to obtain a time zone given its name.

## Parameters

- `allocator`: The allocator object to use to allocate memory for the new time zone. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `name`: The name of the time zone to create.
- `data`: The data to use to initialize the time zone. The contents of the data should be the same as that found within the time-zone files located at `/usr/share/zoneinfo`.

## See Also

### Creating a Time Zone
- [func CFTimeZoneCreateWithName(CFAllocator!, CFString!, Bool) -> CFTimeZone!](./cftimezonecreatewithname%28_,_,_%29.md)
  Returns the time zone object identified by a given name or abbreviation.
- [func CFTimeZoneCreateWithTimeIntervalFromGMT(CFAllocator!, CFTimeInterval) -> CFTimeZone!](./cftimezonecreatewithtimeintervalfromgmt%28_,_%29.md)
  Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecreate(_:_:_:))*