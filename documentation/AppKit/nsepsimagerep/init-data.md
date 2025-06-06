# init(data:)

**Framework**: AppKit  
**Kind**: init

Returns a representation of an image initialized with the specified EPS data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(data epsData: Data)
```

#### Return Value

The initialized `NSEPSImageRep` object or `nil` if the object could not be initialized

#### Discussion

The size of the receiver is set using the bounding box information specified in the EPS header comments.

## Parameters

- `epsData`: The EPS data representing the desired image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsepsimagerep/init(data:))*