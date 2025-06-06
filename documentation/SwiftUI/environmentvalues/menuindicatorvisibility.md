# menuIndicatorVisibility

**Framework**: SwiftUI  
**Kind**: property

The menu indicator visibility to apply to controls within a view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var menuIndicatorVisibility: Visibility { get set }
```

#### Discussion

> **Note**: On tvOS, the standard button styles do not include a menu indicator, so this modifier will have no effect when using a built-in button style. You can implement an indicator in your own [`ButtonStyle`](buttonstyle.md) implementation by checking the value of this environment value.

On tvOS, the standard button styles do not include a menu indicator, so this modifier will have no effect when using a built-in button style. You can implement an indicator in your own [`ButtonStyle`](buttonstyle.md) implementation by checking the value of this environment value.

## See Also

- [func menuIndicator(Visibility) -> some View](view/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/menuindicatorvisibility)*