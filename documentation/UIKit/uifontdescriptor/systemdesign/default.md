# default

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The default typeface for an app’s user interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
static let `default`: UIFontDescriptor.SystemDesign
```

```c
extern UIFontDescriptorSystemDesign const UIFontDescriptorSystemDesignDefault;
```

## Discussion

The returned typeface depends on the system. In iOS, using this constant with [`withDesign(_:)`](../withdesign%28_%29.md) returns SF Pro, while in watchOS that returns SF Compact.

## See Also

### Typeface designs
- [static let rounded: UIFontDescriptor.SystemDesign](./rounded.md)
  The rounded variant of the default typeface.
- [static let monospaced: UIFontDescriptor.SystemDesign](./monospaced.md)
  The monospace variant of the default typeface.
- [static let serif: UIFontDescriptor.SystemDesign](./serif.md)
  The serif variant of the default typeface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/systemdesign/default)*