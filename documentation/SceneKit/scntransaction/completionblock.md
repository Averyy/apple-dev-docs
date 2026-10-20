# completionBlock

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Returns the block previously associated with the current transaction.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class var completionBlock: (() -> Void)? { get set }
```

```objc
@property (class, nonatomic, copy, nullable) void (^completionBlock)();
```

#### Discussion

See `setCompletionBlock(_:)`, `setCompletionBlock:` in Objective-C, for a description of the role of the completion block object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/completionblock)*