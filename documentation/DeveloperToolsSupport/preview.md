# Preview

**Framework**: DeveloperToolsSupport  
**Kind**: struct  
**Role**: Structure

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

## Overview

Frameworks like SwiftUI and WidgetKit define initializers for this type, along with framework-specific preview macros that rely on this type. You don’t use this type directly. Instead, use one of the preview macros, like [`Preview(_:body:)`](../SwiftUI/preview%28_,body%29.md).

## Topics

### Creating a SwiftUI preview
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](./preview/init%28_,traits,body%29-8pemr.md)
  Creates a preview of a SwiftUI view.
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./preview/init%28_,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.
- [init(String?, immersionStyle: some ImmersionStyle, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./preview/init%28_,immersionstyle,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.
- [init(String?, windowStyle: some WindowStyle, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](./preview/init%28_,windowstyle,traits,body,cameras%29.md)
  Creates a preview of a SwiftUI view in a window with custom viewpoints.
### Creating a preview of a widget
- [init<Attributes>(String?, as: ActivityPreviewViewKind, using: Attributes, widget: () -> some Widget, contentStates: () async -> [Attributes.ContentState])](./preview/init%28_,as,using,widget,contentstates%29.md)
  Creates a preview of a live activity widget.
- [init<Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> some Widget, timelineProvider: () -> Provider)](./preview/init%28_,as,using,widget,timelineprovider%29-1if5u.md)
  Creates a preview of a widget with an `AppIntent` configuration.
- [init<Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> some Widget, timelineProvider: () -> Provider)](./preview/init%28_,as,using,widget,timelineprovider%29-5335n.md)
  Creates a preview of a widget with an `INIntent` configuration.
- [init(String?, as: WidgetFamily, widget: () -> some Widget, timeline: () async -> [any TimelineEntry])](./preview/init%28_,as,widget,timeline%29.md)
  Creates a preview of a timeline-style widget.
- [init(String?, as: WidgetFamily, widget: () -> some Widget, timelineProvider: () -> some TimelineProvider)](./preview/init%28_,as,widget,timelineprovider%29.md)
  Creates a preview of a widget with a static configuration.
### Creating an AppKit preview
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSView)](./preview/init%28_,traits,body%29-158mk.md)
  Creates a preview of an NSView.
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSViewController)](./preview/init%28_,traits,body%29-2viaf.md)
  Creates a preview of an NSViewController.
### Getting preview traits
- [Preview.ViewTraits](./preview/viewtraits.md)
  Traits that apply to previews of views and view controllers.
### Initializers
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> any View)](./preview/init%28_,traits,arguments,body%29-1xqo1.md)
  Creates a group of previews of a SwiftUI view.
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIViewController)](./preview/init%28_,traits,arguments,body%29-287km.md)
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIView)](./preview/init%28_,traits,arguments,body%29-3q0i9.md)
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> NSViewController)](./preview/init%28_,traits,arguments,body%29-4ieth.md)
  Creates a group of previews of an NSViewController.
- [init<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> NSView)](./preview/init%28_,traits,arguments,body%29-5cb4o.md)
  Creates a group of previews of an NSView.
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> UIView)](./preview/init%28_,traits,body%29-3i54d.md)
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> UIViewController)](./preview/init%28_,traits,body%29-941vb.md)
- [init<Entry>(String?, widget: () -> some Widget, relevanceEntries: () async -> [Entry])](./preview/init%28_,widget,relevanceentries%29.md)
  Creates a preview of a relevance-driven widget.
- [init<Provider>(String?, widget: () -> some Widget, relevanceProvider: () -> Provider)](./preview/init%28_,widget,relevanceprovider%29.md)
  Creates a preview of a relevance-driven widget.
- [init<Provider>(String?, widget: () -> some Widget, relevanceProvider: () -> Provider, relevance: () async -> WidgetRelevance<Provider.Configuration>)](./preview/init%28_,widget,relevanceprovider,relevance%29.md)
  Creates a preview of a relevance-driven widget.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Preview definition
- [enum PreviewLayout](./previewlayout.md)
  A size constraint for a preview.
- [struct PreviewTrait](./previewtrait.md)
  Customizations that you can apply to a preview.
- [protocol PreviewRegistry](./previewregistry.md)
  A protocol that the system uses to locate previews at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview)*