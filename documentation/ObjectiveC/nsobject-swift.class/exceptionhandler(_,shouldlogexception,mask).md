# exceptionHandler(_:shouldLogException:mask:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Implemented by the delegate to evaluate whether the delegating exception hangler should log a given exception.

**Availability**:
- macOS

## Declaration

```swift
func exceptionHandler(_ sender: NSExceptionHandler!, shouldLogException exception: NSException!, mask aMask: Int) -> Bool
```

```objc
- (BOOL) exceptionHandler:(NSExceptionHandler *) sender shouldLogException:(NSException *) exception mask:(NSUInteger) aMask;
```

#### Return Value

[`YES`](../yes.md) to have the [`NSExceptionHandler`](../../ExceptionHandling/nsexceptionhandler.md) object log the exception, [`NO`](../no.md) otherwise.

## Parameters

- `sender`: The [`NSExceptionHandler`](../../ExceptionHandling/nsexceptionhandler.md) object sending the message.
- `exception`: An [`NSException`](../../Foundation/nsexception.md) object describing the exception to be evaluated.
- `aMask`: The bit mask indicating the types of exceptions logged by the [`NSExceptionHandler`](../../ExceptionHandling/nsexceptionhandler.md) object. See Logging and Handling Constants and System Hang Constants for descriptions of the possible `enum` constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exceptionhandler(_:shouldlogexception:mask:))*