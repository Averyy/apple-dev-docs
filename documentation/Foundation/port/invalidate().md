# invalidate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Marks the receiver as invalid and posts an [`didBecomeInvalidNotification`](./didbecomeinvalidnotification.md) to the default notification center.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func invalidate()
```

```objc
- (void) invalidate;
```

## Discussion

You must call this method before releasing a port object (or removing strong references to it if your application is garbage collected).

## See Also

### Validation
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether the receiver is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/port/invalidate())*