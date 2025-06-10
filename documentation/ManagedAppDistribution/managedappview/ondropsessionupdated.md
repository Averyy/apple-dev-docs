# onDropSessionUpdated(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Specifies an action to perform on each update of an ongoing drop operation activated by `dropDestination(_:)` or other drop modifiers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func onDropSessionUpdated(_ onUpdate: @escaping (DropSession) -> Void) -> some View
```

#### Discussion

The `onUpdate` closure is called when the closest drop session in the child view hierarchy becomes active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/ondropsessionupdated(_:))*