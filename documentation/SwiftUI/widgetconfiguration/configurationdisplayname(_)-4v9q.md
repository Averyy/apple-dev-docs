# configurationDisplayName(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the localized name shown for a widget when a user adds or edits the widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency func configurationDisplayName(_ displayNameKey: LocalizedStringKey) -> some WidgetConfiguration
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func configurationDisplayName(_ displayName: LocalizedStringResource) -> some WidgetConfiguration
```

```swift
@MainActor
@preconcurrency func configurationDisplayName(_ displayName: Text) -> some WidgetConfiguration
```

```swift
@MainActor
@preconcurrency func configurationDisplayName<S>(_ displayName: S) -> some WidgetConfiguration where S : StringProtocol
```

## Return Value

A widget configuration that includes a descriptive name for the widget.

## Parameters

- `displayNameKey`: The key for the localized name to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/configurationdisplayname(_:)-4v9q)*