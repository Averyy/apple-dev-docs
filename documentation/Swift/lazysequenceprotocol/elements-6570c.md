# elements

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

A sequence containing the same elements as this one, possibly with a simpler type.

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
var elements: Self.Elements { get }
```

#### Discussion

When implementing lazy operations, wrapping `elements` instead of `self` can prevent result types from growing an extra `LazySequence` layer.

Note: this property need not be implemented by conforming types, it has a default implementation in a protocol extension that just returns `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequenceprotocol/elements-6570c)*