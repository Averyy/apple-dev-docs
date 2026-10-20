# collaborationModeRestrictions

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
static let collaborationModeRestrictions: UIActivityItemsConfigurationMetadataKey
```

```c
extern UIActivityItemsConfigurationMetadataKey const UIActivityItemsConfigurationMetadataKeyCollaborationModeRestrictions;
```

## See Also

### Constants
- [static let title: UIActivityItemsConfigurationMetadataKey](./title.md)
  A key for the title.
- [static let messageBody: UIActivityItemsConfigurationMetadataKey](./messagebody.md)
  A key for the message body.
- [static let linkPresentationMetadata: UIActivityItemsConfigurationMetadataKey](./linkpresentationmetadata.md)
- [static let shareRecipients: UIActivityItemsConfigurationMetadataKey](./sharerecipients.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey/collaborationmoderestrictions)*