# handleError(_:userInteractionPermitted:)

**Framework**: UIKit  
**Kind**: method

Handles an error that occurs during an attempt to read, save, or revert a document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func handleError(_ error: any Error, userInteractionPermitted: Bool)
```

#### Discussion

Typical [`UIDocument`](uidocument.md) subclasses don’t need to call or override this method. Instead, they can observe the [`stateChangedNotification`](uidocument/statechangednotification.md) notification to be notified of changes in document state. In their notification handler, they can check the value of the [`documentState`](uidocument/documentstate.md) property and proceed accordingly. See [`Resolve conflicts and handle errors`](uidocument#Resolve-conflicts-and-handle-errors.md) for a discussion of this.

If you’re using managed documents (instances of the [`UIManagedDocument`](uimanageddocument.md) subclass), you must subclass this method and, if desired, the [`finishedHandlingError(_:recovered:)`](uidocument/finishedhandlingerror(_:recovered:).md) method. Subclassing allows your app to observe errors in saving or validation. The [`stateChangedNotification`](uidocument/statechangednotification.md) notification doesn’t contain a `userInfo` dictionary and so doesn’t convey specific error information.

If you directly call any of the advanced reading and writing methods that have an error-object parameter (for example, [`writeContents(_:andAttributes:safelyTo:for:)`](uidocument/writecontents(_:andattributes:safelyto:for:).md)) and that call returns an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object by indirection, you should call this method ([`handleError(_:userInteractionPermitted:)`](uidocument/handleerror(_:userinteractionpermitted:).md)), passing in the error object.

This method is called by the default implementations of [`open(completionHandler:)`](uidocument/open(completionhandler:).md) and [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) when [`UIDocument`](uidocument.md) encounters a reading or writing error, respectively.

If you override this method and don’t invoke the superclass implementation (`super`), you’re responsible for the following:

- Calling [`finishedHandlingError(_:recovered:)`](uidocument/finishedhandlingerror(_:recovered:).md) when you’re finished handling the error — for example, when the application doesn’t require any additional user feedback about the error.
- Implementing [`userInteractionNoLongerPermitted(forError:)`](uidocument/userinteractionnolongerpermitted(forerror:).md) to conclude error handling immediately. If `userInteractionPermitted` is [`false`](https://developer.apple.com/documentation/swift/false), you should immediately handle the error and call [`finishedHandlingError(_:recovered:)`](uidocument/finishedhandlingerror(_:recovered:).md) within the context of the [`handleError(_:userInteractionPermitted:)`](uidocument/handleerror(_:userinteractionpermitted:).md).

## Parameters

- `error`: An object encapsulating information about an error encountered in an attempt to open, save, or revert a document. The error domain is  . The error code is one of the   constants declared in  .
- `userInteractionPermitted`: If  , no attempt is (or should be) made to present a modal view to the user. This value can be   in cases such as when a save operation fails while the application is being suspended. If this parameter is  , UIKit or your override may present error information to the user in a modal view and (optionally) allow the user to resolve the error.

## See Also

- [func finishedHandlingError(any Error, recovered: Bool)](uidocument/finishedhandlingerror(_:recovered:).md)
  Tells UIKit that you finished handling the error.
- [func userInteractionNoLongerPermitted(forError: any Error)](uidocument/userinteractionnolongerpermitted(forerror:).md)
  Indicates when it’s no longer safe to proceed without immediately handling the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/handleerror(_:userinteractionpermitted:))*