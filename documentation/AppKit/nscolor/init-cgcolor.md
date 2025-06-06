# init(cgColor:)

**Framework**: AppKit  
**Kind**: init

Creates a color object using the specified Core Graphics color.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init?(cgColor: CGColor)
```

#### Return Value

An `NSColor` instance.

#### Discussion

This method may return `nil`.

## Parameters

- `cgColor`: The Core Graphics color reference.

## See Also

- [convenience init(Color)](nscolor/init(_:).md)
- [init(CIColor: CIColor)](nscolor/init(cicolor:).md)
  Creates a color object from the specified Core Image color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(cgcolor:))*