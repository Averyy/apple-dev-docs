# shareRecipients

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
static let shareRecipients: UIActivityItemsConfigurationMetadataKey
```

```c
extern UIActivityItemsConfigurationMetadataKey const UIActivityItemsConfigurationMetadataKeyShareRecipients;
```

#### Discussion

A key for an array of INPerson objects representing recipients who will be filled in by default in the compose view if that sharing app supports it.

This might fail to pre-fill correctly if the sharing app chosen by the user can’t recognize the provided person. Also, if a people suggestion is chosen, that suggestion will override this provided value.

## See Also

### Constants
- [static let title: UIActivityItemsConfigurationMetadataKey](./title.md)
  A key for the title.
- [static let messageBody: UIActivityItemsConfigurationMetadataKey](./messagebody.md)
  A key for the message body.
- [static let linkPresentationMetadata: UIActivityItemsConfigurationMetadataKey](./linkpresentationmetadata.md)
- [static let collaborationModeRestrictions: UIActivityItemsConfigurationMetadataKey](./collaborationmoderestrictions.md)
  A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey/sharerecipients)*