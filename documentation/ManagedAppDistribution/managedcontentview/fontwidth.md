# fontWidth(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Sets the font width of the text in this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func fontWidth(_ width: Font.Width?) -> some View
```

#### Return Value

A view that uses the font width you specify.

## Parameters

- `width`: One of the available font widths.   Providing   removes the effect of any font width   modifier applied higher in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/fontwidth(_:))*