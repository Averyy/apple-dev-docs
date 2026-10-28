# UIContentView

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The requirements for a content view that you create using a configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UIContentView <NSObject>
```

## Overview

This protocol provides a blueprint for a content view object that renders the content and styling that you define with its configuration. The content view’s configuration encapsulates all of the supported properties and behaviors for content view customization. Setting the content view’s [`configuration`](./uicontentview-5fh3z/configuration.md) property applies the new configuration to the view, causing the view to render any updates to its appearance.

## Topics

### Managing the content configuration
- [configuration](./uicontentview-3zu2k/configuration.md)
  The current configuration of the view.
### Determining configuration support
- [- supportsConfiguration:](./uicontentview-3zu2k/supportsconfiguration_.md)
  Determines whether the view is compatible with the provided configuration.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UIContentUnavailableView](./uicontentunavailableview.md)
- [UIListContentView](./uilistcontentview.md)

## See Also

### Content configurations
- [UIListContentConfiguration](./uilistcontentconfiguration-c.class.md)
  A content configuration for a list-based content view.
- [class UIListContentView](./uilistcontentview.md)
  A content view for displaying list-based content.
- [UIContentConfiguration](./uicontentconfiguration-2raci.md)
  The requirements for an object that provides the configuration for a content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentview-3zu2k)*