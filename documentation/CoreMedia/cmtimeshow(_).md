# CMTimeShow(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Prints a description of the time to the console.

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
func CMTimeShow(_ time: CMTime)
```

```c
extern void CMTimeShow(CMTime time);
```

## Discussion

This function is most appropriate to use for debugging purposes.

## Parameters

- `time`: A time to show.

## See Also

### Representing Times
- [func CMTimeCopyDescription(allocator: CFAllocator?, time: CMTime) -> CFString?](./cmtimecopydescription%28allocator,time%29.md)
  Creates a string representation of the time.
- [func CMTimeCopyAsDictionary(CMTime, allocator: CFAllocator?) -> CFDictionary?](./cmtimecopyasdictionary%28_,allocator%29.md)
  Creates a dictionary representation of the time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeshow(_:))*