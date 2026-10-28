# finishedHandlingError(_:recovered:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells UIKit that you finished handling the error.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func finishedHandlingError(_ error: any Error, recovered: Bool)
```

```objc
- (void) finishedHandlingError:(NSError *) error recovered:(BOOL) recovered;
```

## Discussion

This method is called by default when handling of an error (including any user interaction) is complete. Subclasses need to call this method only if they override [`handleError(_:userInteractionPermitted:)`](./handleerror%28_,userinteractionpermitted%29.md) and do not call the superclass implementation (`super`). If you override this method, you must call `super`.

## Parameters

- `error`: An error object encapsulating information about the error.
- `recovered`: [`true`](../../Swift/true.md) if you recovered from the error, otherwise [`false`](../../Swift/false.md).

## See Also

### Resolving conflicts and handling errors
- [func handleError(any Error, userInteractionPermitted: Bool)](./handleerror%28_,userinteractionpermitted%29.md)
  Handles an error that occurs during an attempt to read, save, or revert a document.
- [func userInteractionNoLongerPermitted(forError: any Error)](./userinteractionnolongerpermitted%28forerror%29.md)
  Indicates when it’s no longer safe to proceed without immediately handling the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/finishedhandlingerror(_:recovered:))*