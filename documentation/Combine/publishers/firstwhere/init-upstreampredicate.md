# init(upstream:predicate:)

**Framework**: Combine  
**Kind**: init

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
init(upstream: Upstream, predicate: @escaping (Publishers.FirstWhere<Upstream>.Output) -> Bool)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/firstwhere/init(upstream:predicate:))*