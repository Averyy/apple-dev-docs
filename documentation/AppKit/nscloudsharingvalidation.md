# NSCloudSharingValidation

**Framework**: AppKit  
**Kind**: protocol

A protocol that a Cloud-sharing toolbar item uses to get validation of an item.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSCloudSharingValidation : NSObjectProtocol
```

## Topics

### Getting an item’s Cloud share
- [func cloudShare(for: any NSValidatedUserInterfaceItem) -> CKShare?](nscloudsharingvalidation/cloudshare(for:).md)
  Returns the Cloud share object that corresponds to the specified item, if one exists.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscloudsharingvalidation)*