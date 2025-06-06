# modifiers(_:)

**Framework**: SwiftUI  
**Kind**: method

Combines a gesture with keyboard modifiers.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func modifiers(_ modifiers: EventModifiers) -> _ModifiersGesture<Self>
```

#### Return Value

A new gesture that combines a gesture with keyboard modifiers.

#### Discussion

The gesture receives updates while the user presses the modifier keys that correspond to the given modifiers option set.

## Parameters

- `modifiers`: A set of flags that correspond to the modifier   keys that the user needs to hold down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/modifiers(_:))*