# buildBlock(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> some ToolbarContent where C0 : ToolbarContent, C1 : ToolbarContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> some CustomizableToolbarContent where C0 : CustomizableToolbarContent, C1 : CustomizableToolbarContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder/buildblock(_:_:)-1fjnr)*