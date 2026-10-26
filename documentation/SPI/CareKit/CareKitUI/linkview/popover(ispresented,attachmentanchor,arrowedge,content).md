---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/popover(ispresented:attachmentanchor:arrowedge:content:)"
framework: "CareKit/CareKitUI"
---

# popover(isPresented:attachmentAnchor:arrowEdge:content:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.popover(isPresented:attachmentAnchor:arrowEdge:content:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
nonisolated
func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/popover(ispresented:attachmentanchor:arrowedge:content:))*