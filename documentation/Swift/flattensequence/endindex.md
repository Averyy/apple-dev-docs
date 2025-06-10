# endIndex

**Framework**: Swift  
**Kind**: property

The collection’s “past the end” position.

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
var endIndex: FlattenSequence<Base>.Index { get }
```

#### Discussion

`endIndex` is not a valid argument to `subscript`, and is always reachable from `startIndex` by zero or more applications of `index(after:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/flattensequence/endindex)*