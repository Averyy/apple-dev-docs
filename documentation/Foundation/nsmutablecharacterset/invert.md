# invert()

**Framework**: Foundation  
**Kind**: method

Replaces all the characters in the receiver with all the characters it didn’t previously contain.

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
func invert()
```

#### Discussion

Inverting a mutable character set, whether by [`invert()`](nsmutablecharacterset/invert().md) or by [`inverted`](nscharacterset/inverted.md), is much less efficient than inverting an immutable character set with [`inverted`](nscharacterset/inverted.md).

## See Also

- [var inverted: CharacterSet](nscharacterset/inverted.md)
  A character set containing only characters that don’t exist in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/invert())*