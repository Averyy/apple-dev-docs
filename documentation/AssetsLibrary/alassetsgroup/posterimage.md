# posterImage()

**Framework**: Assets Library  
**Kind**: method

Returns the group’s poster image

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func posterImage() -> Unmanaged<CGImage>!
```

#### Return Value

The group’s poster image.

#### Discussion

The image is returned in the correct orientation (that is, “pointing up”—you shouldn’t have to rotate the image).

## See Also

- [func value(forProperty: String!) -> Any!](alassetsgroup/value(forproperty:).md)
  Returns the group’s value for a given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/posterimage())*