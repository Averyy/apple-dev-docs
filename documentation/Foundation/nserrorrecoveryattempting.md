# NSErrorRecoveryAttempting

**Framework**: Foundation

A set of methods that provide options to recover from an error.

#### Overview

The `NSErrorRecoveryAttempting` informal protocol provides methods that allow your application to attempt to recover from an error. These methods are invoked when an `NSError` object is returned that specifies the implementing object as the error `recoveryAttempter` and the user has selected one of the error’s localized recovery options. The method invoked depends on how the error is presented to the user. If the error is presented in a document-modal sheet, doc://com.apple.documentation/documentation/objectivec/nsobject/1411071-attemptrecovery is invoked. If the error is presented in an application-modal dialog, doc://com.apple.documentation/documentation/objectivec/nsobject/1416402-attemptrecovery is invoked.

## See Also

- [var recoveryAttempter: Any?](nserror/recoveryattempter.md)
  The object in the user info dictionary corresponding to the [`NSRecoveryAttempterErrorKey`](nsrecoveryattemptererrorkey.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserrorrecoveryattempting)*