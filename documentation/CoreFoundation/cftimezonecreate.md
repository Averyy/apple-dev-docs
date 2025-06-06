# CFTimeZoneCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a time zone with a given name and data.

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
func CFTimeZoneCreate(_ allocator: CFAllocator!, _ name: CFString!, _ data: CFData!) -> CFTimeZone!
```

#### Return Value

A time zone corresponding to `name` and `data`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

You typically do not call this function directly. Use the [`CFTimeZoneCreateWithName(_:_:_:)`](cftimezonecreatewithname(_:_:_:).md) function to obtain a time zone given its name.

## Parameters

- `allocator`: The allocator object to use to allocate memory for the new time zone. Pass   or kCFAllocatorDefault to use the current default allocator.
- `name`: The name of the time zone to create.
- `data`: The data to use to initialize the time zone. The contents of the data should be the same as that found within the time-zone files located at  .

## See Also

- [func CFTimeZoneCreateWithName(CFAllocator!, CFString!, Bool) -> CFTimeZone!](cftimezonecreatewithname(_:_:_:).md)
  Returns the time zone object identified by a given name or abbreviation.
- [func CFTimeZoneCreateWithTimeIntervalFromGMT(CFAllocator!, CFTimeInterval) -> CFTimeZone!](cftimezonecreatewithtimeintervalfromgmt(_:_:).md)
  Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecreate(_:_:_:))*