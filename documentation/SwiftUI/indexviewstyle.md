# IndexViewStyle

**Framework**: SwiftUI  
**Kind**: protocol

Defines the implementation of all `IndexView` instances within a view hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol IndexViewStyle
```

#### Overview

To configure the current `IndexViewStyle` for a view hierarchy, use the `.indexViewStyle()` modifier.

## Topics

### Getting built-in index view styles
- [static var page: PageIndexViewStyle](indexviewstyle/page.md)
  An index view style that places a page index view over its content.
- [static func page(backgroundDisplayMode: PageIndexViewStyle.BackgroundDisplayMode) -> PageIndexViewStyle](indexviewstyle/page(backgrounddisplaymode:).md)
  An index view style that places a page index view over its content.
### Supporting types
- [struct PageIndexViewStyle](pageindexviewstyle.md)
  An index view style that places a page index view over its content.

## Relationships

### Conforming Types
- [PageIndexViewStyle](pageindexviewstyle.md)

## See Also

- [func controlGroupStyle<S>(S) -> some View](view/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [protocol ControlGroupStyle](controlgroupstyle.md)
  Defines the implementation of all control groups within a view hierarchy.
- [struct ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md)
  The properties of a control group.
- [func formStyle<S>(S) -> some View](view/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [protocol FormStyle](formstyle.md)
  The appearance and behavior of a form.
- [struct FormStyleConfiguration](formstyleconfiguration.md)
  The properties of a form instance.
- [func groupBoxStyle<S>(S) -> some View](view/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [protocol GroupBoxStyle](groupboxstyle.md)
  A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [struct GroupBoxStyleConfiguration](groupboxstyleconfiguration.md)
  The properties of a group box instance.
- [func indexViewStyle<S>(S) -> some View](view/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [func labeledContentStyle<S>(S) -> some View](view/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [protocol LabeledContentStyle](labeledcontentstyle.md)
  The appearance and behavior of a labeled content instance..
- [struct LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md)
  The properties of a labeled content instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/indexviewstyle)*