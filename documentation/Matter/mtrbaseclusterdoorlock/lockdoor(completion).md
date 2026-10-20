# lockDoor(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func lockDoor(completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func lockDoor() async throws
```

```objc
- (void) lockDoorWithCompletion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdoorlock/lockdoor(completion:))*