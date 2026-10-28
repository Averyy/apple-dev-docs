# MirrorPath

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A protocol for legitimate arguments to `Mirror`’s `descendant` method.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol MirrorPath
```

## Overview

Do not declare new conformances to this protocol; they will not work as expected.

## Relationships

### Conforming Types
- [Int](./int.md)
- [String](./string.md)

## See Also

### Querying Descendants
- [func descendant(any MirrorPath, any MirrorPath...) -> Any?](./mirror/descendant%28_,_%29.md)
  Returns a specific descendant of the reflected subject, or `nil` if no such descendant exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirrorpath)*