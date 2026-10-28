# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Processes view content for a conditional compiler-control statement that performs an availability check.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@export(implementation)
static func buildLimitedAvailability<Content>(_ content: Content) -> AnyView where Content : View
```

**Other overloads**:

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any Commands) -> some Commands
```

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any CustomizableToolbarContent) -> some CustomizableToolbarContent
```

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any SceneAccessoryContent) -> some SceneAccessoryContent
```

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any ToolbarContent) -> some ToolbarContent
```

```swift
static func buildLimitedAvailability(_ content: some ChartContent) -> AnyChartContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildlimitedavailability(_:)-6alqb)*