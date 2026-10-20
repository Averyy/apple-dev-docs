# userActivityWasContinued(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the user activity was continued on another device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func userActivityWasContinued(_ userActivity: NSUserActivity)
```

```objc
- (void) userActivityWasContinued:(NSUserActivity *) userActivity;
```

## Parameters

- `userActivity`: The user activity that was continued.

## See Also

### Managing activity continuation
- [func userActivityWillSave(NSUserActivity)](./useractivitywillsave%28_%29.md)
  Notifies the delegate that the user activity will be saved to be continued or persisted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/useractivitywascontinued(_:))*