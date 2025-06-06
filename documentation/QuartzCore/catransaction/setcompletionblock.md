# setCompletionBlock(_:)

**Framework**: Core Animation  
**Kind**: method

Sets the completion block object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func setCompletionBlock(_ block: (() -> Void)?)
```

#### Discussion

The completion block object that is guaranteed to be called (on the main thread) as soon as all animations subsequently added by this transaction group have completed (or have been removed.) If no animations are added before the current transaction group is committed (or the completion block is set to a different value,) the block will be invoked immediately.

## Parameters

- `block`: The block object takes no parameters and returns no value.

## See Also

- [class func completionBlock() -> (() -> Void)?](catransaction/completionblock.md)
  Returns the completion block object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/setcompletionblock(_:))*