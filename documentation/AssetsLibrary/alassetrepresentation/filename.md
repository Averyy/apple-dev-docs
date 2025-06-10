# filename()

**Framework**: Assets Library  
**Kind**: method

Returns a string representing the filename of the representation on disk.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func filename() -> String!
```

#### Return Value

A string representing the filename of the representation on disk.

#### Discussion

For representations synced from iTunes, this will be the filename of the representation on the host.

## See Also

- [func orientation() -> ALAssetOrientation](alassetrepresentation/orientation.md)
  Returns the representation’s orientation.
- [func scale() -> Float](alassetrepresentation/scale.md)
  Returns the representation’s scale.
- [func dimensions() -> CGSize](alassetrepresentation/dimensions.md)
  Returns the representation’s dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/filename())*