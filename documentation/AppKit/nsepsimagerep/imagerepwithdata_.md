# imageRepWithData:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a representation of an image initialized with the specified EPS data.

**Availability**:
- macOS 10.0+ - Deprecated in 14.0

## Declaration

```objc
+ (instancetype) imageRepWithData:(NSData *) epsData;
```

#### Return Value

A new, initialized `NSEPSImageRep` object or `nil` if the object could not be initialized.

#### Discussion

The size of the receiver is set using the bounding box information specified in the EPS header comments.

## Parameters

- `epsData`: The EPS data representing the desired image.

## See Also

### Creating Representations of Images from EPS Data
- [init?(data: Data)](./init%28data%29.md)
  Returns a representation of an image initialized with the specified EPS data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsepsimagerep/imagerepwithdata:)*