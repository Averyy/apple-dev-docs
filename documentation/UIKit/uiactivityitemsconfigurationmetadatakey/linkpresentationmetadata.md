# linkPresentationMetadata

**Framework**: UIKit  
**Kind**: property

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
static let linkPresentationMetadata: UIActivityItemsConfigurationMetadataKey
```

## See Also

- [static let title: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/title.md)
  A key for the title.
- [static let messageBody: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/messagebody.md)
  A key for the message body.
- [static let shareRecipients: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/sharerecipients.md)
- [static let collaborationModeRestrictions: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/collaborationmoderestrictions.md)
  A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey/linkpresentationmetadata)*