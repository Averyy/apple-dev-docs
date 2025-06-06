# resourceImage(name:)

**Framework**: TVMLKit  
**Kind**: method

Returns the image for the given resource

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func resourceImage(name resourceName: String) -> UIImage?
```

#### Return Value

The [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) associated with the resource name. Returns `nil` if no image matches the resource name or if the event is not handled.

#### Discussion

The `resourceName` parameter comes from a resource URL specified in certain elements. For example, `<``badge src="resource://developer-resource">` contains the resource name, `developer-resource`.

## Parameters

- `resourceName`: A string that contains the name of the resource.

## See Also

- [func resourceURL(name: String) -> URL?](tvinterfacecreating/resourceurl(name:).md)
  Returns a URL for the given resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/resourceimage(name:))*