# CMTimebaseCreateWithSourceClock(allocator:sourceClock:timebaseOut:)

**Framework**: Core Media  
**Kind**: func

Creates a timebase by using a source clock.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimebaseCreateWithSourceClock(allocator: CFAllocator?, sourceClock: CMClock, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus
```

## Parameters

- `allocator`: The allocator to use for creating the timebase.
- `sourceClock`: The source clock.
- `timebaseOut`: Receives the timebase the function creates.

## See Also

- [func CMTimebaseCreateWithSourceTimebase(allocator: CFAllocator?, sourceTimebase: CMTimebase, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](cmtimebasecreatewithsourcetimebase(allocator:sourcetimebase:timebaseout:).md)
  Creates a timebase by using a source timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasecreatewithsourceclock(allocator:sourceclock:timebaseout:))*