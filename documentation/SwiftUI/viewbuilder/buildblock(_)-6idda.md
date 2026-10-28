# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> TupleContent<repeat each Content>
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<Content>(_ content: Content) -> Content
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

```swift
static func buildBlock<each C>(_ content: repeat each C) -> AnyChartContent where repeat each C : ChartContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildblock(_:)-6idda)*