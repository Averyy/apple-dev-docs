# UIContentConfiguration

**Framework**: UIKit  
**Kind**: protocol

The requirements for an object that provides the configuration for a content view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
protocol UIContentConfiguration
```

#### Overview

This protocol provides a blueprint for a content-configuration object, which encompasses default styling and content for a content view. The content configuration encapsulates all of the supported properties and behaviors for content view customization. You use the configuration to create the content view.

## Topics

### Creating a content configuration
- [func makeContentView() -> any UIView & UIContentView](uicontentconfiguration-9eib5/makecontentview.md)
  Creates a new instance of the content view using this configuration.
### Updating a content configuration
- [func updated(for: any UIConfigurationState) -> Self](uicontentconfiguration-9eib5/updated(for:).md)
  Generates a configuration for the specified state by applying the configuration’s default values for that state to any properties that you haven’t customized.

## Relationships

### Conforming Types
- [UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md)
- [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md)

## See Also

- [struct UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md)
  A content configuration for a list-based content view.
- [class UIListContentView](uilistcontentview.md)
  A content view for displaying list-based content.
- [protocol UIContentView](uicontentview-5fh3z.md)
  The requirements for a content view that you create using a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentconfiguration-9eib5)*