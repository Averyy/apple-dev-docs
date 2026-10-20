# inverted

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSCharacterSet * invertedSet;
```

#### Discussion

Using the inverse of an immutable character set is much more efficient than inverting a mutable character set.

## See Also

### Related Documentation
- [func invert()](../nsmutablecharacterset/invert%28%29.md)
  Replaces all the characters in the receiver with all the characters it didn’t previously contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/inverted)*