# selectedDrawingTool

**Framework**: PaperKit  
**Kind**: property

The currently selected drawing tool.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var selectedDrawingTool: any PKTool { get set }
```

#### Discussion

Default is `PKInkingTool(.monoline)`


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/selecteddrawingtool)*