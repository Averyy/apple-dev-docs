# currentTip

**Framework**: TipKit  
**Kind**: property

Returns the current tip available for display.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
final var currentTip: (any Tip)? { get }
```

## See Also

- [var currentTipUpdates: some AsyncSequence<any Tip, Never>](tipgroup/currenttipupdates.md)
  Stream of tips that become eligible for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipgroup/currenttip)*