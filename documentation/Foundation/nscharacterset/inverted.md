# inverted

**Framework**: Foundation  
**Kind**: property

A character set containing only characters that don’t exist in the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var inverted: CharacterSet { get }
```

#### Discussion

Using the inverse of an immutable character set is much more efficient than inverting a mutable character set.

## See Also

- [func invert()](nsmutablecharacterset/invert.md)
  Replaces all the characters in the receiver with all the characters it didn’t previously contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/inverted)*