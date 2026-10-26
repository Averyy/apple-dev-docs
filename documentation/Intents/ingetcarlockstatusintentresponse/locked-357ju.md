# locked

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating the status of the car’s locks.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- watchOS 3.2+

## Declaration

```swift
@nonobjc
final var locked: Bool? { get set }
```

#### Discussion

Typically, you assign a value to this property only after handling the intent. If the car is locked, set the property to [`true`](../../Swift/true.md); otherwise, set it to [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarlockstatusintentresponse/locked-357ju)*