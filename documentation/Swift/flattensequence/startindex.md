# startIndex

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The position of the first element in a non-empty collection.

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
var startIndex: FlattenSequence<Base>.Index { get }
```

Available when `Base` conforms to `Collection` and `Base.Element` conforms to `Collection`.

## Discussion

In an empty collection, `startIndex == endIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/flattensequence/startindex)*