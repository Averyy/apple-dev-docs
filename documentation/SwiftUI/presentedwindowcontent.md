# PresentedWindowContent

**Framework**: SwiftUI  
**Kind**: struct

A view that represents the content of a presented window.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct PresentedWindowContent<Data, Content> where Data : Decodable, Data : Encodable, Data : Hashable, Content : View
```

#### Overview

You don’t create this type directly. [`WindowGroup`](windowgroup.md) creates values for you.

## Relationships

### Conforms To
- [View](view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentedwindowcontent)*