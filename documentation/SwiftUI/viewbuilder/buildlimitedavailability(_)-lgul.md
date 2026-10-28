# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Builds a partial result that propagates or erases type information outside a compiler-controlled availability check.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildLimitedAvailability(_ content: some ChartContent) -> AnyChartContent
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
@export(implementation)
static func buildLimitedAvailability<Content>(_ content: Content) -> AnyView where Content : View
```

## Discussion

This method provides support for `if` statements with `#available()` clauses in multi-statement closures, producing content for the conditionally-available branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildlimitedavailability(_:)-lgul)*