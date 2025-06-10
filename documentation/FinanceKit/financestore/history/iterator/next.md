# next()

**Framework**: FinanceKit  
**Kind**: method

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func next() async throws -> FinanceStore.Changes<Model>?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/history/iterator/next())*