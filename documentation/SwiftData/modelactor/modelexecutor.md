# modelExecutor

**Framework**: SwiftData  
**Kind**: property  
**Required**: Yes

The executor that coordinates access to the model actor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
nonisolated
var modelExecutor: any ModelExecutor { get }
```

#### Discussion

> ❗ **Important**: Don’t use the executor to access the model context. Instead, use the [`modelContext`](modelactor/modelcontext.md) property.

## See Also

- [var unownedExecutor: UnownedSerialExecutor](modelactor/unownedexecutor.md)
  The optimized, unonwned reference to the model actor’s executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelactor/modelexecutor)*