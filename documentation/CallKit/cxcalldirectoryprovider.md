# CXCallDirectoryProvider

**Framework**: CallKit  
**Kind**: class

The principal object for a Call Directory app extension for a host app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
class CXCallDirectoryProvider
```

## Mentions

- [Identifying and blocking calls](identifying-and-blocking-calls.md)

## Topics

### Beginning a Request
- [func beginRequest(with: CXCallDirectoryExtensionContext)](cxcalldirectoryprovider/beginrequest(with:).md)
  Tells the extension to prepare for a host app’s request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Identifying and blocking calls](identifying-and-blocking-calls.md)
  Create a Call Directory app extension to identify and block incoming callers by their phone number.
- [class CXCallDirectoryExtensionContext](cxcalldirectoryextensioncontext.md)
  A programmatic interface for adding identification and blocking entries to a Call Directory app extension.
- [protocol CXCallDirectoryExtensionContextDelegate](cxcalldirectoryextensioncontextdelegate.md)
  A collection of methods a Call Directory extension context object calls when a request fails.
- [class CXCallDirectoryManager](cxcalldirectorymanager.md)
  The programmatic interface to an object that manages a Call Directory app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryprovider)*