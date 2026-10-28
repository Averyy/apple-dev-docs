# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any SceneAccessoryContent) -> some SceneAccessoryContent
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildlimitedavailability(_:)-2tex4)*