# userActivityWillSave(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the user activity will be saved to be continued or persisted.

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
optional func userActivityWillSave(_ userActivity: NSUserActivity)
```

```objc
- (void) userActivityWillSave:(NSUserActivity *) userActivity;
```

## Discussion

The delegate overrides this method to update the activity with current state.

## Parameters

- `userActivity`: The user activity to update.

## See Also

### Managing activity continuation
- [func userActivityWasContinued(NSUserActivity)](./useractivitywascontinued%28_%29.md)
  Notifies the delegate that the user activity was continued on another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/useractivitywillsave(_:))*