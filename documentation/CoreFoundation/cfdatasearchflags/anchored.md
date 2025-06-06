# anchored

**Framework**: Core Foundation  
**Kind**: property

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var anchored: CFDataSearchFlags { get }
```

#### Discussion

Performs searching only on bytes at the beginning or, if `kCFDataSearchBackwards` is also specified, at the end of the search range. No match at the beginning or end means nothing is found, even if a matching sequence of bytes occurs elsewhere in the data object.

## See Also

- [static var backwards: CFDataSearchFlags](cfdatasearchflags/backwards.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatasearchflags/anchored)*