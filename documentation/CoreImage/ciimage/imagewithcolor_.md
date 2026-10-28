# imageWithColor:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates and returns an image of infinite extent whose entire content is the specified color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (CIImage *) imageWithColor:(CIColor *) color;
```

## Return Value

The image object initialized with the color represented by the [`CIColor`](../cicolor.md) object.

## Parameters

- `color`: A color object.

## See Also

### Creating Solid Colors
- [init(color: CIColor)](./init%28color%29.md)
  Initializes an image of infinite extent whose entire content is the specified color.
- [class var black: CIImage](./black.md)
- [class var blue: CIImage](./blue.md)
- [class var clear: CIImage](./clear.md)
- [class var cyan: CIImage](./cyan.md)
- [class var gray: CIImage](./gray.md)
- [class var green: CIImage](./green.md)
- [class var magenta: CIImage](./magenta.md)
- [class var red: CIImage](./red.md)
- [class var white: CIImage](./white.md)
- [class var yellow: CIImage](./yellow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/imagewithcolor:)*