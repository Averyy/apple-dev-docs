# invalidate()

**Framework**: Exposure Notification  
**Kind**: method

Stops any outstanding operations and invalidates the manager.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
func invalidate()
```

#### Discussion

> ❗ **Important**:  This method is available in iOS 12.5, and in iOS 13.5 and later.

Once you call this method, the object can no longer be used. To start using [`ENManager`](enmanager.md) again, create and activate a new instance of the class.

## Topics

### Completion Handlers
- [var invalidationHandler: (() -> Void)?](enmanager/invalidationhandler.md)
  The handler that the framework invokes when invalidation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/invalidate())*