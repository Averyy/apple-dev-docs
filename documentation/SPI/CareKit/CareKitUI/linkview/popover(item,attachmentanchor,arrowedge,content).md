---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/popover(item:attachmentanchor:arrowedge:content:)"
framework: "CareKit/CareKitUI"
---

# popover(item:attachmentAnchor:arrowEdge:content:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.popover(item:attachmentAnchor:arrowEdge:content:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
nonisolated
func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ViewBuilder content: @escaping (Item) -> Content) -> some View where Item : Identifiable, Content : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/popover(item:attachmentanchor:arrowedge:content:))*