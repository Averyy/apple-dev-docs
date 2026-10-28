# Configurations

**Framework**: UIKit  
**Role**: API Collection

Specify the appearance and content of your views and cells using configurations.

## Overview

Configurations provide a lightweight way to apply content and styling to views without having to manage the rendering of the appearance yourself.

Using a configuration, you can obtain system default styling for a variety of different view states and customize that styling as needed. Then, you assign that configuration to a view that supports configurations, like [`UICollectionViewCell`](./uicollectionviewcell.md), or use it to create a custom content view, like [`UIListContentView`](./uilistcontentview.md). The configuration updates itself when the view’s configuration state changes, causing the view to reflect the new styling for that state.

There are two types of configurations:

- Background configurations, which let you specify the background appearance for a view. For more information, see `UIBackgroundConfiguration`.
- Content configurations, which let you specify content (like image and text) and styling for that content (like tint color and padding). For list-based content, [`UIListContentConfiguration`](./uilistcontentconfiguration-swift.struct.md) defines many customization options.

## Topics

### Configuration states
- [struct UIViewConfigurationState](./uiviewconfigurationstate-swift.struct.md)
  A structure that encapsulates a view’s state.
- [struct UICellConfigurationState](./uicellconfigurationstate-swift.struct.md)
  A structure that encapsulates a cell’s state.
- [protocol UIConfigurationState](./uiconfigurationstate-8d7pd.md)
  The requirements for an object that encapsulates a view’s state.
- [struct UIConfigurationStateCustomKey](./uiconfigurationstatecustomkey.md)
  A key that defines a custom state for a view.
- [UIViewConfigurationState](./uiviewconfigurationstate-c.class.md)
  A structure that encapsulates a view’s state.
- [UICellConfigurationState](./uicellconfigurationstate-c.class.md)
  An object that encapsulates a cell’s state.
- [UIConfigurationState](./uiconfigurationstate-1smq1.md)
  The requirements for an object that encapsulates a view’s state.
### Content configurations
- [struct UIListContentConfiguration](./uilistcontentconfiguration-swift.struct.md)
  A content configuration for a list-based content view.
- [class UIListContentView](./uilistcontentview.md)
  A content view for displaying list-based content.
- [protocol UIContentConfiguration](./uicontentconfiguration-9eib5.md)
  The requirements for an object that provides the configuration for a content view.
- [protocol UIContentView](./uicontentview-5fh3z.md)
  The requirements for a content view that you create using a configuration.
- [UIListContentConfiguration](./uilistcontentconfiguration-c.class.md)
  A content configuration for a list-based content view.
- [UIContentConfiguration](./uicontentconfiguration-2raci.md)
  The requirements for an object that provides the configuration for a content view.
- [UIContentView](./uicontentview-3zu2k.md)
  The requirements for a content view that you create using a configuration.
### Unavailable content configurations
- [struct UIContentUnavailableConfiguration](./uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.
- [struct UIContentUnavailableConfigurationState](./uicontentunavailableconfigurationstate-swift.struct.md)
  A structure that encapsulates state for a content-unavailable view.
- [UIContentUnavailableConfiguration](./uicontentunavailableconfiguration-c.class.md)
  A content configuration for a content-unavailable view.
- [UIContentUnavailableConfigurationState](./uicontentunavailableconfigurationstate-c.class.md)
  An object that encapsulates state for a content-unavailable view.
- [UIContentUnavailableButtonProperties](./uicontentunavailablebuttonproperties.md)
  Properties configuring the appearance and behavior of a button in a content-unavailable view.
- [UIContentUnavailableImageProperties](./uicontentunavailableimageproperties.md)
  Properties configuring the appearance of images in a content-unavailable view.
- [UIContentUnavailableTextProperties](./uicontentunavailabletextproperties.md)
  Properties configuring the appearance of text in a content-unavailable view.
- [UIContentUnavailableAlignment](./uicontentunavailablealignment.md)
  Defines the alignment of views in a content-unavailable view.
### Background configurations
- [struct UIBackgroundConfiguration](./uibackgroundconfiguration-swift.struct.md)
  A configuration that describes a specific background appearance.
- [UIBackgroundConfiguration](./uibackgroundconfiguration-c.class.md)
  A configuration that describes a specific background appearance.
### Color transformers
- [struct UIConfigurationColorTransformer](./uiconfigurationcolortransformer-swift.struct.md)
  A transformer that generates a modified output color from an input color.
- [UIConfigurationColorTransformer](./uiconfigurationcolortransformer-c.typealias.md)
  Generates a modified output color from an input color.
### Text attributes transformers
- [struct UIConfigurationTextAttributesTransformer](./uiconfigurationtextattributestransformer-swift.struct.md)
  Defines a text transformation that can affect the visual appearance of a string.
- [UIConfigurationTextAttributesTransformer](./uiconfigurationtextattributestransformer-c.typealias.md)
  Defines a text transformation that can affect the visual appearance of a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/configurations)*