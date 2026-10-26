# imageRepWithData:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a representation of an image from the specified data in the PICT file format.

**Availability**:
- macOS

## Declaration

```objc
+ (instancetype) imageRepWithData:(NSData *) pictData;
```

#### Return Value

An initialized [`NSPICTImageRep`](../nspictimagerep.md), or `nil` if the object could not be initialized. Initialization may fail if the data does not conform to the PICT file format.

## Parameters

- `pictData`: A data object containing the PICT data.

## See Also

### Related Documentation
- [var pictRepresentation: Data](./pictrepresentation.md)
  The image representation’s PICT data.
### Creating Representations of Images from PICT Data
- [init?(data: Data)](./init%28data%29.md)
  Returns a representation of an image from the specified data in the PICT file format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspictimagerep/imagerepwithdata:)*