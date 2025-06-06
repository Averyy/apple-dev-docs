# RequestError

**Framework**: CKTool JS  
**Kind**: struct

An object that represents a general error from the service.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary RequestError {
	Int32 code;
	string message;
	string reason;
	string? detailedMessage;
	string? requestUuid;
	Int32? retryAfterSeconds;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { RequestError } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [code](requesterror/code.md)
  The HTTP status code for a request error.
- [detailedMessage](requesterror/detailedmessage.md)
  A string that contains any additional information about this error.
- [message](requesterror/message.md)
  A string containing the code for the error that occurred.
- [reason](requesterror/reason.md)
  A string that indicates the reason for the error.
- [requestUuid](requesterror/requestuuid.md)
  A unique identifier for this error.
- [retryAfterSeconds](requesterror/retryafterseconds.md)
  The suggested time to wait in seconds before trying this operation again.

## See Also

- [AuthenticationRequiredError](authenticationrequirederror.md)
  An object that represents an error that occurs when authentication information is missing for the current user.
- [CKDBBatchDeleteError](ckdbbatchdeleteerror.md)
  An object that represents an error that may occur when deleting a resource as part of a batch delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/requesterror)*