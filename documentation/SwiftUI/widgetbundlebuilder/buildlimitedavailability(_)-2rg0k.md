# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Processes widget content for a conditional compiler-control statement that performs an availability check.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
@export(implementation)
static func buildLimitedAvailability(_ widget: some Widget) -> any Widget & _LimitedAvailabilityWidgetMarker
```

**Other overloads**:

```swift
@export(implementation)
static func buildLimitedAvailability(_ widget: some ControlWidget) -> any Widget & _LimitedAvailabilityWidgetMarker
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildlimitedavailability(_:)-2rg0k)*