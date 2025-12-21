# init(_:as:widget:timelineProvider:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a preview of a widget with a static configuration.

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
init(_ name: String? = nil, as family: WidgetFamily, widget: @escaping () -> some Widget, timelineProvider: @escaping () -> some TimelineProvider)
```

#### Discussion

The `#Preview` macro expands into a declaration that calls this initializer. To create a preview that appears in the canvas, you must use the macro, not instantiate a Preview directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:as:widget:timelineprovider:))*