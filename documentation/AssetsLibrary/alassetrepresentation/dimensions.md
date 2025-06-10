# dimensions()

**Framework**: Assets Library  
**Kind**: method

Returns the representation’s dimensions.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func dimensions() -> CGSize
```

#### Return Value

The representation’s dimensions.

#### Discussion

If the representation doesn’t have valid dimensions, this method will return [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero).

## See Also

- [func orientation() -> ALAssetOrientation](alassetrepresentation/orientation.md)
  Returns the representation’s orientation.
- [func scale() -> Float](alassetrepresentation/scale.md)
  Returns the representation’s scale.
- [func filename() -> String!](alassetrepresentation/filename.md)
  Returns a string representing the filename of the representation on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/dimensions())*