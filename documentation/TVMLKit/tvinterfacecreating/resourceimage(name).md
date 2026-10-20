# resourceImage(name:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Returns the image for the given resource

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func resourceImage(name resourceName: String) -> UIImage?
```

```objc
- (UIImage *) imageForResource:(NSString *) resourceName;
```

#### Return Value

The [`UIImage`](../../UIKit/uiimage.md) associated with the resource name. Returns `nil` if no image matches the resource name or if the event is not handled.

#### Discussion

The `resourceName` parameter comes from a resource URL specified in certain elements. For example, `<``badge src="resource://developer-resource">` contains the resource name, `developer-resource`.

## Parameters

- `resourceName`: A string that contains the name of the resource.

## See Also

### Retrieving Resource Information
- [func resourceURL(name: String) -> URL?](./resourceurl%28name%29.md)
  Returns a URL for the given resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/resourceimage(name:))*