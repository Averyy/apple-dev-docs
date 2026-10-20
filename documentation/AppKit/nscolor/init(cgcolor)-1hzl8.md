# init(cgColor:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object using the specified Core Graphics color.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init?(cgColor: CGColor)
```

```objc
+ (NSColor *) colorWithCGColor:(CGColorRef) cgColor;
```

#### Return Value

An `NSColor` instance.

#### Discussion

This method may return `nil`.

## Parameters

- `cgColor`: The Core Graphics color reference.

## See Also

### Converting other types of color objects
- [convenience init(Color)](./init%28_%29.md)
- [init(CIColor: CIColor)](./init%28cicolor%29-3rxsk.md)
  Creates a color object from the specified Core Image color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(cgcolor:)-1hzl8)*