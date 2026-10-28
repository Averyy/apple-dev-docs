# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.0+
- watchOS 10.5+

## Declaration

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any CustomizableToolbarContent) -> some CustomizableToolbarContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any Commands) -> some Commands
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
@export(implementation)
static func buildLimitedAvailability<Content>(_ content: Content) -> AnyView where Content : View
```

```swift
static func buildLimitedAvailability(_ content: some ChartContent) -> AnyChartContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildlimitedavailability(_:)-6wsqg)*