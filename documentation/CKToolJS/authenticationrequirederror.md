# AuthenticationRequiredError

**Framework**: CKTool JS  
**Kind**: struct

An object that represents an error that occurs when authentication information is missing for the current user.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary AuthenticationRequiredError {
	Int32 code;
	string message;
	string reason;
	string? detailedMessage;
	string? requestUuid;
	Int32? retryAfterSeconds;
	string redirectUrl;
};
```

#### Overview

Some database operations require that users sign in with their Apple ID. The server returns `AuthenticationRequiredError` when the user isn’t signed in or their session has expired.

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { AuthenticationRequiredError } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [code](authenticationrequirederror/code.md)
  The HTTP status code for a request error.
- [detailedMessage](authenticationrequirederror/detailedmessage.md)
  A string that contains any additional information about this error.
- [message](authenticationrequirederror/message.md)
  A string containing the code for the error that occurred.
- [reason](authenticationrequirederror/reason.md)
  A string that indicates the reason for the error.
- [redirectUrl](authenticationrequirederror/redirecturl.md)
  A redirect URL for the user to securely sign in using their Apple ID.
- [requestUuid](authenticationrequirederror/requestuuid.md)
  A unique identifier for this error.
- [retryAfterSeconds](authenticationrequirederror/retryafterseconds.md)
  The suggested time to wait in seconds before trying this operation again.

## See Also

- [CKDBBatchDeleteError](ckdbbatchdeleteerror.md)
  An object that represents an error that may occur when deleting a resource as part of a batch delete operation.
- [RequestError](requesterror.md)
  An object that represents a general error from the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/authenticationrequirederror)*