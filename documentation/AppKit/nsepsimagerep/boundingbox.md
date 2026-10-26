# boundingBox

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle that bounds the image representation.

**Availability**:
- macOS 10.0+ - Deprecated in 14.0

> **Deprecated**: `NSEPSImageRep` instances cannot be created on macOS 14.0 and later

## Declaration

```swift
var boundingBox: NSRect { get }
```

```objc
@property (readonly) NSRect boundingBox;
```

## See Also

### Related Documentation
- [init?(data: Data)](./init%28data%29.md)
  Returns a representation of an image initialized with the specified EPS data.
- [+ imageRepWithData:](./imagerepwithdata_.md)
  Creates and returns a representation of an image initialized with the specified EPS data.
### Getting Data
- [var epsRepresentation: Data](./epsrepresentation.md)
  The EPS representation of the image representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsepsimagerep/boundingbox)*