# predicate

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The closure that determines whether to publish an element.

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
let predicate: (Publishers.FirstWhere<Upstream>.Output) -> Bool
```

## See Also

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/firstwhere/predicate)*