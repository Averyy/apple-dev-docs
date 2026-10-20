# textStorageObserver

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The observer for the text storage object.

**Availability**:
- macOS 12.0+

## Declaration

```swift
weak var textStorageObserver: (any NSTextStorageObserving)? { get set }
```

```objc
@property (weak, nullable) id<NSTextStorageObserving> textStorageObserver;
```

## See Also

### Accessing the storage controller
- [protocol NSTextStorageObserving](../nstextstorageobserving.md)
  Optional methods that delegates implement to handle editing and transaction processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/textstorageobserver)*