# description(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the description shown for a widget when a user adds or edits it using the specified string.

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
@preconcurrency func description<S>(_ description: S) -> some WidgetConfiguration where S : StringProtocol
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
@preconcurrency func description(_ descriptionResource: LocalizedStringResource) -> some WidgetConfiguration
```

## Return Value

A widget configuration with a description of the widget.

## Parameters

- `description`: A string describing the widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/description(_:)-2bfr)*