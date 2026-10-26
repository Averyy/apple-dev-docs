# UIContentConfiguration

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The requirements for an object that provides the configuration for a content view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UIContentConfiguration <NSObject, NSCopying>
```

#### Overview

This protocol provides a blueprint for a content-configuration object, which encompasses default styling and content for a content view. The content configuration encapsulates all of the supported properties and behaviors for content view customization. You use the configuration to create the content view.

## Topics

### Creating a content configuration
- [- makeContentView](./uicontentconfiguration-2raci/makecontentview.md)
  Creates a new instance of the content view using this configuration.
### Updating a content configuration
- [- updatedConfigurationForState:](./uicontentconfiguration-2raci/updatedconfigurationforstate_.md)
  Generates a configuration for the specified state by applying the configuration’s default values for that state to any properties that you haven’t customized.

## Relationships

### Inherits From
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UIContentUnavailableConfiguration](./uicontentunavailableconfiguration-c.class.md)
- [UIListContentConfiguration](./uilistcontentconfiguration-c.class.md)

## See Also

### Content configurations
- [UIListContentConfiguration](./uilistcontentconfiguration-c.class.md)
  A content configuration for a list-based content view.
- [class UIListContentView](./uilistcontentview.md)
  A content view for displaying list-based content.
- [UIContentView](./uicontentview-3zu2k.md)
  The requirements for a content view that you create using a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentconfiguration-2raci)*