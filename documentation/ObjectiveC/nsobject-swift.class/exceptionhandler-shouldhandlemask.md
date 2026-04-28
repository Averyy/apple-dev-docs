# exceptionHandler(_:shouldHandle:mask:)

**Framework**: Objective-C Runtime  
**Kind**: method

Implemented by the delegate to evaluate whether the delegating exception handler should handle a given exception.

**Availability**:
- macOS ?+

## Declaration

```swift
func exceptionHandler(_ sender: NSExceptionHandler!, shouldHandle exception: NSException!, mask aMask: Int) -> Bool
```

#### Return Value

[`YES`](yes.md) to have the doc://com.apple.documentation/documentation/exceptionhandling/nsexceptionhandler object handle the exception, [`NO`](no.md) otherwise.

## Parameters

- `sender`: The doc://com.apple.documentation/documentation/exceptionhandling/nsexceptionhandler object sending the message.
- `exception`: An [`NSException`](https://developer.apple.com/documentation/Foundation/NSException) object describing the exception to be evaluated.
- `aMask`: The bit mask indicating the types of exceptions handled by the doc://com.apple.documentation/documentation/exceptionhandling/nsexceptionhandler object. See Logging and Handling Constants and System Hang Constants for descriptions of the possible `enum` constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exceptionhandler(_:shouldhandle:mask:))*