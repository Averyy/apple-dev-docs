# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> some AccessibilityRotorContent where repeat each Content : AccessibilityRotorContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<Content>(_ content: Content) -> Content
```

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> TupleContent<repeat each Content>
```

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> TupleView<(repeat each Content)> where repeat each Content : View
```

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> some Commands where repeat each Content : Commands
```

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> some CustomizableToolbarContent where repeat each Content : CustomizableToolbarContent
```

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> some ToolbarContent where repeat each Content : ToolbarContent
```

```swift
static func buildBlock<each C>(_ content: repeat each C) -> AnyChartContent where repeat each C : ChartContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildblock(_:)-6fpke)*