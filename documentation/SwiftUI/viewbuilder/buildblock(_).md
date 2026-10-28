# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Passes a single piece of content written as a child view through unmodified.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<Content>(_ content: Content) -> Content
```

**Other overloads**:

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

```swift
static func buildBlock<each C>(_ content: repeat each C) -> AnyChartContent where repeat each C : ChartContent
```

## Discussion

An example of a single item written as child content is `{ Text("Hello") }`.

## See Also

### Building content
- [static buildBlock()](./buildblock%28%29.md)
  Builds an empty content from a block containing no statements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildblock(_:))*