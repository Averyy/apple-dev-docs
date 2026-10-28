# messageBody

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key for the message body.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let messageBody: UIActivityItemsConfigurationMetadataKey
```

```c
extern UIActivityItemsConfigurationMetadataKey const UIActivityItemsConfigurationMetadataKeyMessageBody;
```

## Discussion

The value of this key is an [`NSString`](../../Foundation/nsstring.md) or [`NSAttributedString`](../../Foundation/nsattributedstring.md) that contains the message body.

## See Also

### Constants
- [static let title: UIActivityItemsConfigurationMetadataKey](./title.md)
  A key for the title.
- [static let linkPresentationMetadata: UIActivityItemsConfigurationMetadataKey](./linkpresentationmetadata.md)
- [static let shareRecipients: UIActivityItemsConfigurationMetadataKey](./sharerecipients.md)
- [static let collaborationModeRestrictions: UIActivityItemsConfigurationMetadataKey](./collaborationmoderestrictions.md)
  A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey/messagebody)*