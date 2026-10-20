# init(viewing:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

View initialized raw memory as a span of bytes.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
init(viewing bytes: RawSpan)
```

Available when `Element` is `UInt8`.

## Parameters

- `bytes`: An existing `RawSpan`, which will define both this `Span`’s lifetime and the memory it represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span/init(viewing:)-9d31g)*