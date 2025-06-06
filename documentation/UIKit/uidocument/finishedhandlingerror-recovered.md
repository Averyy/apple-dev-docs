# finishedHandlingError(_:recovered:)

**Framework**: UIKit  
**Kind**: method

Tells UIKit that you finished handling the error.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func finishedHandlingError(_ error: any Error, recovered: Bool)
```

#### Discussion

This method is called by default when handling of an error (including any user interaction) is complete. Subclasses need to call this method only if they override [`handleError(_:userInteractionPermitted:)`](uidocument/handleerror(_:userinteractionpermitted:).md) and do not call the superclass implementation (`super`). If you override this method, you must call `super`.

## Parameters

- `error`: An error object encapsulating information about the error.
- `recovered`:   if you recovered from the error, otherwise  .

## See Also

- [func handleError(any Error, userInteractionPermitted: Bool)](uidocument/handleerror(_:userinteractionpermitted:).md)
  Handles an error that occurs during an attempt to read, save, or revert a document.
- [func userInteractionNoLongerPermitted(forError: any Error)](uidocument/userinteractionnolongerpermitted(forerror:).md)
  Indicates when it’s no longer safe to proceed without immediately handling the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/finishedhandlingerror(_:recovered:))*