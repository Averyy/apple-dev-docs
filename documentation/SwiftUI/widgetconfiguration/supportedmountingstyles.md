# supportedMountingStyles(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the mounting style for this widget.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func supportedMountingStyles(_ styles: [WidgetMountingStyle]) -> some WidgetConfiguration
```

#### Return Value

A widget configuration that supports the specified mounting styles.

#### Discussion

The mounting style view modifier only has an effect to widgets in visionOS, including widgets of compatible widgets of compatible iOS or iPadOS apps.

```swift
struct MySpatialWidget: Widget {
     let kind: String = "MySpatialWidget"

     var body: some WidgetConfiguration {
         AppIntentConfiguration(kind: kind, intent: ConfigurationIntent.self, provider: Provider()) { entry in
             EntryView(entry: entry)
                .containerBackground(.fill.tertiary, for: .widget)
         }
         .supportedFamilies([.systemSmall, .systemLarge])
         .supportedMountingStyles([.recessed])
     }
}
```

The above code defines a widget that only supports the recessed mounting style.

The mounting style view modifier only has an effect to widgets in visionOS, including widgets of compatible widgets of compatible iOS or iPadOS apps.

## Parameters

- `styles`: The set of mounting styles that the widget supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/supportedmountingstyles(_:))*