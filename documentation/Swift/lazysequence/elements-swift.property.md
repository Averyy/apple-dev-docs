# elements

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The `Base` (presumably non-lazy) sequence from which `self` was created.

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
var elements: LazySequence<Base>.Elements { get }
```

Available when `Base` conforms to `Sequence`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequence/elements-swift.property)*