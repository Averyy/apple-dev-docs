# asyncAndWait(flags:execute:)

**Framework**: Dispatch  
**Kind**: method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+
- watchOS 5.0+

## Declaration

```swift
func asyncAndWait<T>(flags: DispatchWorkItemFlags, execute work: () throws -> T) rethrows -> T
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncandwait(flags:execute:))*