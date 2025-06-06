# CMTimeCopyDescription(allocator:time:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

A string representation of the time.

## Parameters

- `allocator`: An allocator with which to create the description. Pass   to use the default allocator.
- `time`: The time to describe.

## See Also

- [func CMTimeShow(CMTime)](cmtimeshow(_:).md)
  Prints a description of the time to the console.
- [func CMTimeCopyAsDictionary(CMTime, allocator: CFAllocator?) -> CFDictionary?](cmtimecopyasdictionary(_:allocator:).md)
  Creates a dictionary representation of the time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimecopydescription(allocator:time:))*