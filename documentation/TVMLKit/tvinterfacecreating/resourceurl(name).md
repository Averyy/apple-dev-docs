# resourceURL(name:)

**Framework**: TVMLKit  
**Kind**: method

Returns a URL for the given resource.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func resourceURL(name resourceName: String) -> URL?
```

#### Return Value

The URL associated with the resource name. The app must return `nil` if the event is not handled.

#### Discussion

The `resourceName` parameter comes from a resource URL specified in certain elements. For example, `badge src="resource://developer-resource">` contains the resource name, `developer-resource`.

## Parameters

- `resourceName`: A string that contains the name of the resource.

## See Also

- [func resourceImage(name: String) -> UIImage?](tvinterfacecreating/resourceimage(name:).md)
  Returns the image for the given resource


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/resourceurl(name:))*