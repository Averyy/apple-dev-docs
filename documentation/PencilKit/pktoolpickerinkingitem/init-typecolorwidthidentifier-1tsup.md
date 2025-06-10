# init(type:color:width:identifier:)

**Framework**: PencilKit  
**Kind**: init

Create a new inking tool item.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
convenience init(type: PKInkingTool.InkType, color: NSColor? = nil, width: CGFloat? = nil, identifier: String? = nil)
```

## Parameters

- `type`: The ink type for the tool.
- `color`: The color for the tool. Passing   resolves to a default value based on the  .
- `width`: The width for the tool. Passing   resolves to a default value based on the  .
- `identifier`: The identifier for the tool item. Passing   resolves to a default value based on the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickerinkingitem/init(type:color:width:identifier:)-1tsup)*