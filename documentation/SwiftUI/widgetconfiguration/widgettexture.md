# widgetTexture(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the widget texture for this widget.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func widgetTexture(_ material: WidgetTexture) -> some WidgetConfiguration
```

#### Return Value

A widget configuration using the specified widget texture.

#### Discussion

Every widget when rendered in visionOS will have a material treatment applied. By default, all widgets use the `glass` widget texture. Use this modifier to explicitly set the widget texture for a widget.

The following displays a widget whose texture is paper:

```swift
AppIntentConfiguration(
    kind: kind, intent: LatestPostConfiguration.self, provider: Provider()
) { entry in
    LatestPostsView(entry: entry)
}
.widgetTexture(.paper)
```

- Parameters texture: The texture to be used when rendering this widget


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/widgettexture(_:))*