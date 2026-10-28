# AppLibrary.App.Metadata

**Framework**: MarketplaceKit  
**Kind**: struct  
**Role**: Structure

Information about an app’s version and account.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct Metadata
```

## Overview

The [`installedMetadata`](./installedmetadata.md) property of the [`AppLibrary.App`](../app.md) class is of this type.

## Topics

### Inspecting app metadata
- [let account: String?](./metadata/account.md)
- [let appleVersionID: AppleVersionID](./metadata/appleversionid.md)
- [let shortVersion: String](./metadata/shortversion.md)
- [let version: String](./metadata/version.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting an app’s version and account
- [var installedMetadata: AppLibrary.App.Metadata?](./installedmetadata.md)
  The app version and the account that’s installing the app


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app/metadata)*