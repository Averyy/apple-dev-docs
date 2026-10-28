# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
static func buildBlock<each C>(_ content: repeat each C) -> AnyChartContent where repeat each C : ChartContent
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
static func buildBlock<each Content>(_ content: repeat each Content) -> some AccessibilityRotorContent where repeat each Content : AccessibilityRotorContent
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildblock(_:)-91ku4)*