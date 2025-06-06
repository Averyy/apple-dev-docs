# backgroundColors

**Framework**: AppKit  
**Kind**: property

The array of background colors to use when drawing the grid.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var backgroundColors: [NSColor]! { get set }
```

#### Discussion

The [`NSColor`](nscolor.md) objects in this property are used to draw the grid’s background. The appearance of the background depends on the value you specify:

- Specifying `nil` fills the background with the collection view’s default background color.
- Specifying an empty array causes the collection view to draw no background color.
- Specifying an array with one color object fills the background with the specified color.
- Specifying an array with more than one color object causes the collection view to use the specified colors to create a checkerboard pattern. Each successive grid item is displayed with the next color in the array, cycling back to the beginning of the array when the last color is reached.

The default value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewgridlayout/backgroundcolors)*