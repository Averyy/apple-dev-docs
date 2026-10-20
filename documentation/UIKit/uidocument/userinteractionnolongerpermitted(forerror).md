# userInteractionNoLongerPermitted(forError:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Indicates when it’s no longer safe to proceed without immediately handling the error.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func userInteractionNoLongerPermitted(forError error: any Error)
```

```objc
- (void) userInteractionNoLongerPermittedForError:(NSError *) error;
```

#### Discussion

UIKit calls this method when it’s no longer safe to proceed without immediately handling the error, such as when the application is being suspended. Subclasses that override this method must immediately end error handling (including dismissing any interactive user interface) and call [`finishedHandlingError(_:recovered:)`](./finishedhandlingerror%28_,recovered%29.md) before returning. It’s only necessary to override this method if you override [`handleError(_:userInteractionPermitted:)`](./handleerror%28_,userinteractionpermitted%29.md) without invoking the superclass implementation (`super`).

## Parameters

- `error`: An error object encapsulating information about the error.

## See Also

### Resolving conflicts and handling errors
- [func handleError(any Error, userInteractionPermitted: Bool)](./handleerror%28_,userinteractionpermitted%29.md)
  Handles an error that occurs during an attempt to read, save, or revert a document.
- [func finishedHandlingError(any Error, recovered: Bool)](./finishedhandlingerror%28_,recovered%29.md)
  Tells UIKit that you finished handling the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/userinteractionnolongerpermitted(forerror:))*