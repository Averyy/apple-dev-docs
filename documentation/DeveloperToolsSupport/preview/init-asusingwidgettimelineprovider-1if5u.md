# init(_:as:using:widget:timelineProvider:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a preview of a widget with an `AppIntent` configuration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 26.0+ (Beta)
- watchOS 10.0+

## Declaration

```swift
@MainActor
init<Provider>(_ name: String? = nil, as family: WidgetFamily, using intent: Provider.Intent, widget: @escaping () -> some Widget, timelineProvider: @escaping () -> Provider) where Provider : AppIntentTimelineProvider
```

#### Discussion

The `#Preview` macro expands into a declaration that calls this initializer. To create a preview that appears in the canvas, you must use the macro, not instantiate a Preview directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:as:using:widget:timelineprovider:)-1if5u)*