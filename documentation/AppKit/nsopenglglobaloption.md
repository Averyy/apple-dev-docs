# NSOpenGLGlobalOption

**Framework**: AppKit  
**Kind**: enum

Constants that specify OpenGL options.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum NSOpenGLGlobalOption
```

#### Overview

These constants are option names for [`NSOpenGLSetOption`](nsopenglsetoption.md) and [`NSOpenGLGetOption`](nsopenglgetoption.md).

## Topics

### Constants
- [NSOpenGLGlobalOption.formatCacheSize](nsopenglglobaloption/formatcachesize.md)
  Sets the size of the pixel format cache.
- [NSOpenGLGlobalOption.clearFormatCache](nsopenglglobaloption/clearformatcache.md)
  Resets the pixel format cache if true.
- [NSOpenGLGlobalOption.retainRenderers](nsopenglglobaloption/retainrenderers.md)
  Whether to retain loaded renderers in memory.
- [NSOpenGLGlobalOption.useBuildCache](nsopenglglobaloption/usebuildcache.md)
  Whether to enable the function compilation block cache. This is off by default. It must be enabled at startup.
### Deprecated
- [var globalValue: GLint](nsopenglglobaloption/globalvalue.md)
### Initializers
- [init?(rawValue: UInt32)](nsopenglglobaloption/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum NSMultibyteGlyphPacking](nsmultibyteglyphpacking.md)
  A constant for glyph packing.
- [Glyph Attributes](glyph-attributes.md)
  Attributes that are used only inside the glyph generation machinery, but must also be shared between components.
- [Data Entry Types](data-entry-types.md)
  These constants specify how a cell formats numeric data.
- [Anonymous](nsbuttontypes-anonymous.md)
- [Additional Writing Directions](additional-writing-directions.md)
  Additional values to be added to [`NSWritingDirection.leftToRight`](nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](nswritingdirection/righttoleft.md), when used with `NSAttributedString/Key/writingDirection`.
- [Return values for modal operations](return-values-for-modal-operations.md)
  Historical return values for [`runModal(for:)`](nsapplication/runmodal(for:).md) and [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md).
- [Tags of Views in the FontPanel](tags-of-views-in-the-fontpanel.md)
  These constants are obsolete and should not be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglglobaloption)*