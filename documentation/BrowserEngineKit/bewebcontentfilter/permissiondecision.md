# BEWebContentFilter.PermissionDecision

**Framework**: BrowserEngineKit  
**Kind**: enum  
**Role**: Enumeration

The outcome of a request to add a blocked URL to the web content filter’s allow list.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
enum PermissionDecision
```

```c
enum BEWebContentFilterPermissionDecision : NSInteger;
```

## Overview

The [`requestPermission(for:referrerURL:presenting:completionHandler:)`](./requestpermission%28for,referrerurl,presenting,completionhandler%29.md) method sends an instance of this enumeration to its completion handler.

## Topics

### Determining the result
- [BEWebContentFilter.PermissionDecision.allowed](./permissiondecision/allowed.md)
  A value that indicates a guardian approves the request and the system can add the URL to the allow list.
- [BEWebContentFilter.PermissionDecision.denied](./permissiondecision/denied.md)
  A value that indicates a guardian denies the request.
- [BEWebContentFilter.PermissionDecision.pending](./permissiondecision/pending.md)
  A value that indicates the request awaits a guardian’s response.
- [BEWebContentFilter.PermissionDecision.error](./permissiondecision/error.md)
  A value that indicates the system fails to retrieve a decision.
### Creating a permission decision
- [init?(rawValue: Int)](./permissiondecision/init%28rawvalue%29.md)
  Creates a decision with the specified permission value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting permission for a blocked URL
- [func requestPermission(for: URL, referrerURL: URL?, presenting: UIView?, completionHandler: (BEWebContentFilter.PermissionDecision, (any Error)?) -> Void)](./requestpermission%28for,referrerurl,presenting,completionhandler%29.md)
  Requests permission to add a blocked URL to the web content filter’s allow list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/permissiondecision)*