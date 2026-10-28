# NSErrorRecoveryAttempting

**Framework**: Foundation

A set of methods that provide options to recover from an error.

## Overview

The `NSErrorRecoveryAttempting` informal protocol provides methods that allow your application to attempt to recover from an error. These methods are invoked when an `NSError` object is returned that specifies the implementing object as the error `recoveryAttempter` and the user has selected one of the error’s localized recovery options. The method invoked depends on how the error is presented to the user. If the error is presented in a document-modal sheet, [`attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)`](../ObjectiveC/nsobject-swift.class/attemptrecovery%28fromerror,optionindex,delegate,didrecoverselector,contextinfo%29.md) is invoked. If the error is presented in an application-modal dialog, [`attemptRecovery(fromError:optionIndex:)`](../ObjectiveC/nsobject-swift.class/attemptrecovery%28fromerror,optionindex%29.md) is invoked.

## Topics

### Attempting Recovery From Errors
- [func attemptRecovery(fromError: any Error, optionIndex: Int, delegate: Any?, didRecoverSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)](../ObjectiveC/nsobject-swift.class/attemptrecovery%28fromerror,optionindex,delegate,didrecoverselector,contextinfo%29.md)
  Implemented to attempt a recovery from an error noted in a document-modal sheet.
- [func attemptRecovery(fromError: any Error, optionIndex: Int) -> Bool](../ObjectiveC/nsobject-swift.class/attemptrecovery%28fromerror,optionindex%29.md)
  Implemented to attempt a recovery from an error noted in an application-modal dialog.

## See Also

### Getting the Error Recovery Attempter
- [var recoveryAttempter: Any?](./nserror/recoveryattempter.md)
  The object in the user info dictionary corresponding to the [`NSRecoveryAttempterErrorKey`](./nsrecoveryattemptererrorkey.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserrorrecoveryattempting)*