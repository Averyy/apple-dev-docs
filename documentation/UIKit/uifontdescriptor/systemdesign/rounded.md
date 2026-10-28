# rounded

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The rounded variant of the default typeface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
static let rounded: UIFontDescriptor.SystemDesign
```

```c
extern UIFontDescriptorSystemDesign const UIFontDescriptorSystemDesignRounded;
```

## Discussion

The returned typeface depends on the system. iOS returns SF Pro Rounded, while watchOS returns SF Compact Rounded.

## See Also

### Typeface designs
- [static let `default`: UIFontDescriptor.SystemDesign](./default.md)
  The default typeface for an app’s user interface.
- [static let monospaced: UIFontDescriptor.SystemDesign](./monospaced.md)
  The monospace variant of the default typeface.
- [static let serif: UIFontDescriptor.SystemDesign](./serif.md)
  The serif variant of the default typeface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/systemdesign/rounded)*