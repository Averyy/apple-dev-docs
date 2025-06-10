# completionBlock

**Framework**: SceneKit  
**Kind**: property

Returns the block previously associated with the current transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class var completionBlock: (() -> Void)? { get set }
```

#### Discussion

See `setCompletionBlock(_:)`, `setCompletionBlock:` in Objective-C, for a description of the role of the completion block object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/completionblock)*