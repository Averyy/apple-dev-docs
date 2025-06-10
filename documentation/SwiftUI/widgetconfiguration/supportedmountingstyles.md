# supportedMountingStyles(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the mounting style for this widget.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func supportedMountingStyles(_ styles: [WidgetMountingStyle]) -> some WidgetConfiguration
```

#### Return Value

A widget configuration that supports the mounting styles specified.

#### Discussion

iOS widgets implementing this style will only see this style as an iOS widget on visionOS.

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

The above code defines a widget that will support only recessed mounting style.

- Parameters mountingStyles: The set of mounting styles the widget supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/supportedmountingstyles(_:))*