# init(_:in:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init?<S>(_ range: NSRange, in string: S) where S : StringProtocol
```

Available when `Bound` is `String.Index`.

## See Also

### Converting Ranges
- [func relative<C>(to: C) -> Range<Bound>](./relative%28to%29.md)
  Returns the range of indices described by this range expression within the given collection.
- [init?(NSRange, in: String)](./init%28_,in%29-5cclx.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/init(_:in:)-5qfor)*