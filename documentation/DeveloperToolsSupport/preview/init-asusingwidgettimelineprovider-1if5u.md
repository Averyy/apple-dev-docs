# init(_:as:using:widget:timelineProvider:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a preview of a widget with an `AppIntent` configuration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
init<Provider>(_ name: String? = nil, as family: WidgetFamily, using intent: Provider.Intent, widget: @escaping () -> some Widget, timelineProvider: @escaping () -> Provider) where Provider : AppIntentTimelineProvider
```

#### Discussion

The `#Preview` macro expands into a declaration that calls this initializer. To create a preview that appears in the canvas, you must use the macro, not instantiate a Preview directly.

## See Also

- [init<Attributes>(String?, as: ActivityPreviewViewKind, using: Attributes, widget: () -> some Widget, contentStates: () async -> [Attributes.ContentState])](preview/init(_:as:using:widget:contentstates:).md)
  Creates a preview of a live activity widget.
- [init<Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> some Widget, timelineProvider: () -> Provider)](preview/init(_:as:using:widget:timelineprovider:)-5335n.md)
  Creates a preview of a widget with an `INIntent` configuration.
- [init(String?, as: WidgetFamily, widget: () -> some Widget, timeline: () async -> [any TimelineEntry])](preview/init(_:as:widget:timeline:).md)
  Creates a preview of a timeline-style widget.
- [init(String?, as: WidgetFamily, widget: () -> some Widget, timelineProvider: () -> some TimelineProvider)](preview/init(_:as:widget:timelineprovider:).md)
  Creates a preview of a widget with a static configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:as:using:widget:timelineprovider:)-1if5u)*