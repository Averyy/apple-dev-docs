# CMTimeCopyDescription(allocator:time:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a string representation of the time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimeCopyDescription(allocator: CFAllocator?, time: CMTime) -> CFString?
```

```c
extern CFStringRefCMTimeCopyDescription(CFAllocatorRef allocator, CMTime time);
```

#### Return Value

A string representation of the time.

## Parameters

- `allocator`: An allocator with which to create the description. Pass [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) to use the default allocator.
- `time`: The time to describe.

## See Also

### Representing Times
- [func CMTimeShow(CMTime)](./cmtimeshow%28_%29.md)
  Prints a description of the time to the console.
- [func CMTimeCopyAsDictionary(CMTime, allocator: CFAllocator?) -> CFDictionary?](./cmtimecopyasdictionary%28_,allocator%29.md)
  Creates a dictionary representation of the time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimecopydescription(allocator:time:))*