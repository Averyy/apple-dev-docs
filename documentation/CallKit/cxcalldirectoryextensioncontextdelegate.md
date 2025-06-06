# CXCallDirectoryExtensionContextDelegate

**Framework**: CallKit  
**Kind**: protocol

A collection of methods a Call Directory extension context object calls when a request fails.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol CXCallDirectoryExtensionContextDelegate : NSObjectProtocol
```

## Topics

### Handling Request Failures
- [func requestFailed(for: CXCallDirectoryExtensionContext, withError: any Error)](cxcalldirectoryextensioncontextdelegate/requestfailed(for:witherror:).md)
  Called when a Call Directory app extension request fails.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Identifying and blocking calls](identifying-and-blocking-calls.md)
  Create a Call Directory app extension to identify and block incoming callers by their phone number.
- [class CXCallDirectoryProvider](cxcalldirectoryprovider.md)
  The principal object for a Call Directory app extension for a host app.
- [class CXCallDirectoryExtensionContext](cxcalldirectoryextensioncontext.md)
  A programmatic interface for adding identification and blocking entries to a Call Directory app extension.
- [class CXCallDirectoryManager](cxcalldirectorymanager.md)
  The programmatic interface to an object that manages a Call Directory app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontextdelegate)*