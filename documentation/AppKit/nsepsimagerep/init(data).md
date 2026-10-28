# init(data:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a representation of an image initialized with the specified EPS data.

**Availability**:
- macOS 10.0+ - Deprecated in 14.0

> **Deprecated**: `NSEPSImageRep` instances cannot be created on macOS 14.0 and later

## Declaration

```swift
init?(data epsData: Data)
```

```objc
- (instancetype) initWithData:(NSData *) epsData;
```

## Return Value

The initialized `NSEPSImageRep` object or `nil` if the object could not be initialized

## Discussion

The size of the receiver is set using the bounding box information specified in the EPS header comments.

## Parameters

- `epsData`: The EPS data representing the desired image.

## See Also

### Creating Representations of Images from EPS Data
- [+ imageRepWithData:](./imagerepwithdata_.md)
  Creates and returns a representation of an image initialized with the specified EPS data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsepsimagerep/init(data:))*