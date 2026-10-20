# invertColor(_:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Type Method

Converts a color from light to dark appearance or vice versa.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class func invertColor(_ color: CGColor) -> Unmanaged<CGColor>
```

```objc
+ (CGColorRef) invertColor:(CGColorRef) color;
```

#### Return Value

The inverted color.

#### Discussion

This has the same effect as `convertColor` with opposite user interface styles.

## Parameters

- `color`: The color to be inverted light<->dark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/invertcolor(_:))*