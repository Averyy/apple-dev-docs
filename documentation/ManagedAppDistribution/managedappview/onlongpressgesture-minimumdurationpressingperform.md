# onLongPressGesture(minimumDuration:pressing:perform:)

**Framework**: ManagedAppDistribution  
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

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/onlongpressgesture(minimumduration:pressing:perform:))*