# activationRequest(forExtensionWithIdentifier:queue:)

**Framework**: System Extensions  
**Kind**: method

Creates a request to activate a System Extension.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func activationRequest(forExtensionWithIdentifier identifier: String, queue: dispatch_queue_t) -> Self
```

## Mentions

- [Installing System Extensions and Drivers](installing-system-extensions-and-drivers.md)

#### Return Value

A new extension request.

#### Discussion

Create and submit an activation request whenever you want to use a given extension. If the extension is inactive, the system may need to prompt the user for approval. The request succeeds only after the user gives their approval.

If the extension is already active, the request succeeds in short order, without significant delay or user interaction. If you request activation of a new version of an already-active extension, the system prompts the user to resolve the conflict before proceeding.

An activation request may succeed, but also indicate that the extension requires a restart to become active. This can occur when replacing an extension that required a restart to deactivate. The most recently activated extension becomes active when the user restarts their Mac.

## Parameters

- `identifier`: The bundle identifier of the target extension.
- `queue`: The dispatch queue to use when calling delegate methods.

## See Also

- [class func deactivationRequest(forExtensionWithIdentifier: String, queue: dispatch_queue_t) -> Self](ossystemextensionrequest/deactivationrequest(forextensionwithidentifier:queue:).md)
  Creates a request to deactivate a System Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/activationrequest(forextensionwithidentifier:queue:))*