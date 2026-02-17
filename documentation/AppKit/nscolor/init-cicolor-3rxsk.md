# init(CIColor:)

**Framework**: AppKit  
**Kind**: init

Creates a color object from the specified Core Image color.

**Availability**:
- macOS ?+

## Declaration

```swift
init(CIColor color: CIColor)
```

#### Return Value

The `NSColor` object corresponding to the specified Core Image color.

#### Discussion

The method raises if the color space and components associated with `color` are `nil` or invalid.

## Parameters

- `color`: The Core Image color to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(cicolor:)-3rxsk)*