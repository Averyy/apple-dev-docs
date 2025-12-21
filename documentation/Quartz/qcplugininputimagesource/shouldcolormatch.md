# shouldColorMatch()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns whether or not the image source should be color matched.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func shouldColorMatch() -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/Swift/false) if the source is a mask or gradient; [`true`](https://developer.apple.com/documentation/Swift/true) otherwise.

## See Also

- [func imageColorSpace() -> Unmanaged<CGColorSpace>!](qcplugininputimagesource/imagecolorspace.md)
  Returns the color space of the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/shouldcolormatch())*