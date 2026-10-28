# MTLClearColorMake(_:_:_:_:)

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Returns a color value used to clear a color attachment.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MTLClearColorMake(_ red: Double, _ green: Double, _ blue: Double, _ alpha: Double) -> MTLClearColor
```

```c
static MTLClearColor MTLClearColorMake(double red, double green, double blue, double alpha);
```

## Return Value

A value for clearing a color attachment.

## Parameters

- `red`: The red color channel.
- `green`: The green color channel.
- `blue`: The blue color channel.
- `alpha`: The alpha channel.

## See Also

### Specifying clearing value
- [var clearColor: MTLClearColor](./mtlrenderpasscolorattachmentdescriptor/clearcolor.md)
  The color to use when clearing the color attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlclearcolormake(_:_:_:_:))*