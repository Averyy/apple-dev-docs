# delegate

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The object you use to respond to changes in the drawn content or with the selected tool.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any PKCanvasViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<PKCanvasViewDelegate> delegate;
```

## See Also

### Responding to drawing-related changes
- [protocol PKCanvasViewDelegate](../pkcanvasviewdelegate.md)
  Methods for monitoring drawing related changes in a canvas view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasview/delegate)*