# init(type:color:width:azimuth:identifier:)

**Framework**: PencilKit  
**Kind**: init

Create a new inking tool item.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(type: PKInkingTool.InkType, color: UIColor? = nil, width: CGFloat? = nil, azimuth: CGFloat? = nil, identifier: String? = nil)
```

## Parameters

- `type`: The ink type for the tool.
- `color`: The color for the tool. Passing   resolves to a default value based on the  .
- `width`: The width for the tool. Passing   resolves to a default value based on the  .
- `azimuth`: The azimuth for the tool. Passing   resolves to a default value based on the  .
- `identifier`: The identifier for the tool item. Passing   resolves to a default value based on the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickerinkingitem/init(type:color:width:azimuth:identifier:)-7gkxh)*