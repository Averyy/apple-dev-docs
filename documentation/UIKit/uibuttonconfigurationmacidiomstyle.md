# UIButtonConfigurationMacIdiomStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The button style your app uses when running in macOS.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```c
enum UIButtonConfigurationMacIdiomStyle : NSInteger;
```

## Overview

If you build your app with [Mac Catalyst](./mac-catalyst.md), you can use these styles to configure how your app displays a button when running on a Mac. To opt in to these styles, choose Optimize Interface for Mac in you project’s general settings.

If you’re configuring your button in Interface Builder, you can choose a style from the Mac Style pop-up menu in the Attributes inspector.

## Topics

### Button styles
- [UIButtonConfigurationMacIdiomStyleAutomatic](./uibuttonconfigurationmacidiomstyle/uibuttonconfigurationmacidiomstyleautomatic.md)
  The button has a style that matches other content in the button configuration.
- [UIButtonConfigurationMacIdiomStyleBordered](./uibuttonconfigurationmacidiomstyle/uibuttonconfigurationmacidiomstylebordered.md)
  The button has a bordered style.
- [UIButtonConfigurationMacIdiomStyleBorderless](./uibuttonconfigurationmacidiomstyle/uibuttonconfigurationmacidiomstyleborderless.md)
  The button has a borderless style.
- [UIButtonConfigurationMacIdiomStyleBorderlessTinted](./uibuttonconfigurationmacidiomstyle/uibuttonconfigurationmacidiomstyleborderlesstinted.md)
  The button has a tinted, borderless style.

## See Also

### Configuring the appearance on macOS
- [macIdiomStyle](./uibuttonconfiguration/macidiomstyle.md)
  The style to use when this button appears in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfigurationmacidiomstyle)*