# CKDBBatchDeleteError

**Framework**: CKTool JS  
**Kind**: struct

An object that represents an error that may occur when deleting a resource as part of a batch delete operation.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBBatchDeleteError {
	string id;
	string code;
	string message;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBBatchDeleteError } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [code](ckdbbatchdeleteerror/code.md)
  A string that contains the code for the error that occurred.
- [id](ckdbbatchdeleteerror/id.md)
  The identifier for the resource that failed to be deleted.
- [message](ckdbbatchdeleteerror/message.md)
  A string that indicates the reason for the error.

## See Also

- [AuthenticationRequiredError](authenticationrequirederror.md)
  An object that represents an error that occurs when authentication information is missing for the current user.
- [RequestError](requesterror.md)
  An object that represents a general error from the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbbatchdeleteerror)*