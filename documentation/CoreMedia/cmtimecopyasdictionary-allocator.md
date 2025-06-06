# CMTimeCopyAsDictionary(_:allocator:)

**Framework**: Core Media  
**Kind**: func

Creates a dictionary representation of the time.

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
func CMTimeCopyAsDictionary(_ time: CMTime, allocator: CFAllocator?) -> CFDictionary?
```

#### Return Value

A dictionary representation of the time.

## Parameters

- `time`: A time from which to create a dictionary.
- `allocator`: An allocator with which to create the dictionary. Pass   to use the default allocator.

## See Also

- [func CMTimeShow(CMTime)](cmtimeshow(_:).md)
  Prints a description of the time to the console.
- [func CMTimeCopyDescription(allocator: CFAllocator?, time: CMTime) -> CFString?](cmtimecopydescription(allocator:time:).md)
  Creates a string representation of the time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimecopyasdictionary(_:allocator:))*