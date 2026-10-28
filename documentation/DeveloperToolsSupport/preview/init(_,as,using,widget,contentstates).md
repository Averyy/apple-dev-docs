# init(_:as:using:widget:contentStates:)

**Framework**: DeveloperToolsSupport  
**Kind**: init  
**Role**: Initializer

Creates a preview of a live activity widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
init<Attributes>(_ name: String? = nil, as viewKind: ActivityPreviewViewKind, using attributes: Attributes, widget: @escaping () -> some Widget, @PreviewActivityBuilder<Attributes> contentStates: @escaping @MainActor () async -> [Attributes.ContentState]) where Attributes : ActivityAttributes
```

## Discussion

The `#Preview` macro expands into a declaration that calls this initializer. To create a preview that appears in the canvas, you must use the macro, not instantiate a Preview directly.

## See Also

### Creating a preview of a widget
- [init<Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> some Widget, timelineProvider: () -> Provider)](./init%28_,as,using,widget,timelineprovider%29-1if5u.md)
  Creates a preview of a widget with an `AppIntent` configuration.
- [init<Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> some Widget, timelineProvider: () -> Provider)](./init%28_,as,using,widget,timelineprovider%29-5335n.md)
  Creates a preview of a widget with an `INIntent` configuration.
- [init(String?, as: WidgetFamily, widget: () -> some Widget, timeline: () async -> [any TimelineEntry])](./init%28_,as,widget,timeline%29.md)
  Creates a preview of a timeline-style widget.
- [init(String?, as: WidgetFamily, widget: () -> some Widget, timelineProvider: () -> some TimelineProvider)](./init%28_,as,widget,timelineprovider%29.md)
  Creates a preview of a widget with a static configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:as:using:widget:contentstates:))*