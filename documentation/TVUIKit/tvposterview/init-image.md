# init(image:)

**Framework**: TVUIKit  
**Kind**: init

Creates a new poster view using the supplied image.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
init(image: UIImage?)
```

#### Discussion

The size of the poster view is determined by the natural size of the passed image when no frame or content size is explicitly set.

## Parameters

- `image`: The image to be displayed in the content view area of the lockup view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvposterview/init(image:))*