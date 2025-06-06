# default

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

The returned typeface depends on the system. In iOS, using this constant with [`withDesign(_:)`](uifontdescriptor/withdesign(_:).md) returns SF Pro, while in watchOS that returns SF Compact.

## See Also

- [static let rounded: UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign/rounded.md)
  The rounded variant of the default typeface.
- [static let monospaced: UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign/monospaced.md)
  The monospace variant of the default typeface.
- [static let serif: UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign/serif.md)
  The serif variant of the default typeface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/systemdesign/default)*