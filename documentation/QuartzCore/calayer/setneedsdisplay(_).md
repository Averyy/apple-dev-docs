# setNeedsDisplay(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Marks the region within the specified rectangle as needing to be updated.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setNeedsDisplay(_ r: CGRect)
```

```objc
- (void) setNeedsDisplayInRect:(CGRect) r;
```

## Parameters

- `r`: The rectangular region of the layer to mark as invalid. You must specify this rectangle in the layer’s own coordinate system.

## See Also

### Updating layer display
- [func setNeedsDisplay()](./setneedsdisplay%28%29.md)
  Marks the layer’s contents as needing to be updated.
- [var needsDisplayOnBoundsChange: Bool](./needsdisplayonboundschange.md)
  A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Initiates the update process for a layer if it is currently marked as needing an update.
- [func needsDisplay() -> Bool](./needsdisplay%28%29.md)
  Returns a Boolean indicating whether the layer has been marked as needing an update.
- [class func needsDisplay(forKey: String) -> Bool](./needsdisplay%28forkey%29.md)
  Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/setneedsdisplay(_:))*