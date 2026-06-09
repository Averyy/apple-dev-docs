# Preview

**Framework**: DeveloperToolsSupport  
**Kind**: struct

A base type that preview macros use to create previews.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
struct Preview
```

#### Overview

Frameworks like SwiftUI and WidgetKit define initializers for this type, along with framework-specific preview macros that rely on this type. You don’t use this type directly. Instead, use one of the preview macros, like [`Preview(_:body:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:body:)).

## Topics

### Creating a SwiftUI preview
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview/init(_:traits:body:)-8pemr.md)
  Creates a preview of a SwiftUI view.
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview/init(_:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.
- [init(String?, immersionStyle: some ImmersionStyle, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview/init(_:immersionstyle:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.
- [init(String?, windowStyle: some WindowStyle, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview/init(_:windowstyle:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view in a window with custom viewpoints.
### Creating a preview of a widget
- [init<Attributes>(String?, as: ActivityPreviewViewKind, using: Attributes, widget: () -> some Widget, contentStates: () async -> [Attributes.ContentState])](preview/init(_:as:using:widget:contentstates:).md)
  Creates a preview of a live activity widget.
- [init<Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> some Widget, timelineProvider: () -> Provider)](preview/init(_:as:using:widget:timelineprovider:)-1if5u.md)
  Creates a preview of a widget with an `AppIntent` configuration.
- [init<Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> some Widget, timelineProvider: () -> Provider)](preview/init(_:as:using:widget:timelineprovider:)-5335n.md)
  Creates a preview of a widget with an `INIntent` configuration.
- [init(String?, as: WidgetFamily, widget: () -> some Widget, timeline: () async -> [any TimelineEntry])](preview/init(_:as:widget:timeline:).md)
  Creates a preview of a timeline-style widget.
- [init(String?, as: WidgetFamily, widget: () -> some Widget, timelineProvider: () -> some TimelineProvider)](preview/init(_:as:widget:timelineprovider:).md)
  Creates a preview of a widget with a static configuration.
### Creating an AppKit preview
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSView)](preview/init(_:traits:body:)-158mk.md)
  Creates a preview of an NSView.
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSViewController)](preview/init(_:traits:body:)-2viaf.md)
  Creates a preview of an NSViewController.
### Getting preview traits
- [Preview.ViewTraits](preview/viewtraits.md)
  Traits that apply to previews of views and view controllers.
### Initializers
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> any View)](preview/init(_:traits:arguments:body:)-1xqo1.md)
  Creates a group of previews of a SwiftUI view.
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIViewController)](preview/init(_:traits:arguments:body:)-287km.md)
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIView)](preview/init(_:traits:arguments:body:)-3q0i9.md)
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> NSViewController)](preview/init(_:traits:arguments:body:)-4ieth.md)
  Creates a group of previews of an NSViewController.
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> NSView)](preview/init(_:traits:arguments:body:)-5cb4o.md)
  Creates a group of previews of an NSView.
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> UIView)](preview/init(_:traits:body:)-3i54d.md)
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> UIViewController)](preview/init(_:traits:body:)-941vb.md)
- [init<Entry>(String?, widget: () -> some Widget, relevanceEntries: () async -> [Entry])](preview/init(_:widget:relevanceentries:).md)
  Creates a preview of a relevance-driven widget.
- [init<Provider>(String?, widget: () -> some Widget, relevanceProvider: () -> Provider)](preview/init(_:widget:relevanceprovider:).md)
  Creates a preview of a relevance-driven widget.
- [init<Provider>(String?, widget: () -> some Widget, relevanceProvider: () -> Provider, relevance: () async -> WidgetRelevance<Provider.Configuration>)](preview/init(_:widget:relevanceprovider:relevance:).md)
  Creates a preview of a relevance-driven widget.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum PreviewLayout](previewlayout.md)
  A size constraint for a preview.
- [struct PreviewTrait](previewtrait.md)
  Customizations that you can apply to a preview.
- [protocol PreviewRegistry](previewregistry.md)
  A protocol that the system uses to locate previews at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview)*