# description(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the localized description shown for a widget when a user adds or edits the widget.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency func description(_ descriptionResource: LocalizedStringResource) -> some WidgetConfiguration
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func description(_ description: Text) -> some WidgetConfiguration
```

```swift
@MainActor
@preconcurrency func description(_ descriptionKey: LocalizedStringKey) -> some WidgetConfiguration
```

```swift
@MainActor
@preconcurrency func description<S>(_ description: S) -> some WidgetConfiguration where S : StringProtocol
```

## Return Value

A widget configuration with a description of the widget.

## Parameters

- `descriptionResource`: Text resource for the localized description to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/description(_:)-5nywo)*