# CMTimebaseCreateWithSourceTimebase(allocator:sourceTimebase:timebaseOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a timebase by using a source timebase.

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
func CMTimebaseCreateWithSourceTimebase(allocator: CFAllocator?, sourceTimebase: CMTimebase, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus
```

```c
extern OSStatus CMTimebaseCreateWithSourceTimebase(CFAllocatorRef allocator, CMTimebaseRef sourceTimebase, CMTimebaseRef*timebaseOut);
```

## Parameters

- `allocator`: The allocator to use for creating the timebase.
- `sourceTimebase`: The source timebase.
- `timebaseOut`: Receives the timebase the function creates.

## See Also

### Creating Timebases
- [func CMTimebaseCreateWithSourceClock(allocator: CFAllocator?, sourceClock: CMClock, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithsourceclock%28allocator,sourceclock,timebaseout%29.md)
  Creates a timebase by using a source clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasecreatewithsourcetimebase(allocator:sourcetimebase:timebaseout:))*