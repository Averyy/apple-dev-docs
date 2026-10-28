# invalidationHandler

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The handler that the framework invokes when invalidation completes.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var invalidationHandler: (() -> Void)? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) dispatch_block_t invalidationHandler;
```

## Discussion

The framework invokes this handler only once, and clears the property before invoking it to break retain cycles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/invalidationhandler)*