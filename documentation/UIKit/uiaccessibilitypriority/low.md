# low

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A low-priority announcement that the system queues and speaks after other speech utterances are complete.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
static let low: UIAccessibilityPriority
```

```c
extern UIAccessibilityPriority const UIAccessibilityPriorityLow;
```

## See Also

### Choosing a priority
- [static let high: UIAccessibilityPriority](./high.md)
  A high-priority announcement that interrupts other speech and isn’t interruptible after it starts.
- [static let `default`: UIAccessibilityPriority](./default.md)
  A default-priority announcement that interrupts existing speech, but is interruptible if a new speech utterance starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitypriority/low)*