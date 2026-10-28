# configurationDisplayName(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the name shown for a widget when a user adds or edits it using the specified string.

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
@preconcurrency func configurationDisplayName<S>(_ displayName: S) -> some WidgetConfiguration where S : StringProtocol
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
@preconcurrency func configurationDisplayName(_ displayNameKey: LocalizedStringKey) -> some WidgetConfiguration
```

## Return Value

A widget configuration that includes a descriptive name for the widget.

## Parameters

- `displayName`: A string describing the widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/configurationdisplayname(_:)-2c3zv)*