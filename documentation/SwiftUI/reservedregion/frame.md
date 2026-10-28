# frame

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The rectangle that describes the region within your view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
var frame: CGRect { get }
```

## Discussion

The frame uses your view’s own coordinates. It already includes the region’s [`margins`](./margins.md), so you don’t need to add the margins yourself.

## See Also

### Getting the region’s geometry
- [var margins: EdgeInsets](./margins.md)
  The extra space around the reserved area that keeps interactive content clear of it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion/frame)*