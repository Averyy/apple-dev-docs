# init(CIColor:)

**Framework**: AppKit  
**Kind**: init

Creates a color object from the specified Core Image color.

**Availability**:
- macOS ?+

## Declaration

```swift
init(ciColor color: CIColor)
```

#### Return Value

The `NSColor` object corresponding to the specified Core Image color.

#### Discussion

The method raises if the color space and components associated with `color` are `nil` or invalid.

## Parameters

- `color`: The Core Image color to convert.

## See Also

- [convenience init(Color)](nscolor/init(_:).md)
- [init?(cgColor: CGColor)](nscolor/init(cgcolor:).md)
  Creates a color object using the specified Core Graphics color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(cicolor:))*