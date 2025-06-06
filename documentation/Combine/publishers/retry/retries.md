# retries

**Framework**: Combine  
**Kind**: property

The maximum number of retry attempts to perform.

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
let retries: Int?
```

#### Discussion

If `nil`, this publisher attempts to reconnect with the upstream publisher an unlimited number of times.

## See Also

- [let upstream: Upstream](publishers/retry/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/retry/retries)*