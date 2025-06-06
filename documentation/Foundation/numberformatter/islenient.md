# isLenient

**Framework**: Foundation  
**Kind**: property

Determines whether the receiver will use heuristics to guess at the number which is intended by a string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isLenient: Bool { get set }
```

#### Discussion

If the formatter is set to be lenient, as with any guessing it may get the result number wrong (that is, a number other than that which was intended).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/islenient)*