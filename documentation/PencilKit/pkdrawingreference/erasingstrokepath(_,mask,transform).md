# erasingStrokePath(_:mask:transform:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func erasingStrokePath(_ eraserPath: PKStrokePath, mask: UIBezierPath?, transform: CGAffineTransform) -> PKDrawing
```

*macOS*

```swift
func erasingStrokePath(_ eraserPath: PKStrokePath, mask: NSBezierPath?, transform: CGAffineTransform) -> PKDrawing
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (PKDrawing *) drawingByErasingStrokePath:(PKStrokePath *) eraserPath mask:(UIBezierPath *) mask transform:(CGAffineTransform) transform;
```

*macOS*

```objc
- (PKDrawing *) drawingByErasingStrokePath:(PKStrokePath *) eraserPath mask:(NSBezierPath *) mask transform:(CGAffineTransform) transform;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/erasingstrokepath(_:mask:transform:))*