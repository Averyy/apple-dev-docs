# invalidationHandler

**Framework**: Exposure Notification  
**Kind**: property

The handler that the framework invokes when invalidation completes.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var invalidationHandler: (() -> Void)? { get set }
```

#### Discussion

The framework invokes this handler only once, and clears the property before invoking it to break retain cycles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/invalidationhandler)*