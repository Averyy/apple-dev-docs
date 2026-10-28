# withSystemEffect(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new color object that represents the current color modified to include the specified visual effect.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func withSystemEffect(_ systemEffect: NSColor.SystemEffect) -> NSColor
```

```objc
- (NSColor *) colorWithSystemEffect:(NSColorSystemEffect) systemEffect;
```

## Discussion

Instead of defining separate colors for user interactions with a view, use this method to retrieve the appropriate color for use with those interactions. This method blends the current color with an appropriate modifier and returns the results. For example, specifying [`NSColor.SystemEffect.pressed`](./systemeffect/pressed.md) for the `systemEffect` parameter yields the color to use when you want your view to appear as if it had been pressed. This method takes the current appearance into account, returning an appropriately modified color for both light and dark appearances.

## Parameters

- `systemEffect`: The visual effect you want to apply to a view or control.

## See Also

### Applying specific appearances to colors
- [NSColor.SystemEffect](./systemeffect.md)
  Constants for user interactions that change the appearance of a view or control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/withsystemeffect(_:))*