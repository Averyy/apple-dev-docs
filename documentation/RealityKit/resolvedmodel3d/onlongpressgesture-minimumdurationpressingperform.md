# onLongPressGesture(minimumDuration:pressing:perform:)

**Framework**: RealityKit  
**Kind**: method

Adds an action to perform when this view recognizes a long press gesture.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
nonisolated
func onLongPressGesture(minimumDuration: Double = 0.5, pressing: ((Bool) -> Void)? = nil, perform action: @escaping () -> Void) -> some View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/onlongpressgesture(minimumduration:pressing:perform:))*