# init(data:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a representation of an image from the specified data in the PICT file format.

**Availability**:
- macOS

## Declaration

```swift
init?(data pictData: Data)
```

```objc
- (instancetype) initWithData:(NSData *) pictData;
```

## Return Value

An initialized [`NSPICTImageRep`](../nspictimagerep.md), or `nil` if the object could not be initialized. Initialization may fail if the data does not conform to the PICT file format.

## Discussion

If the PICT data is obtained directly from a PICT file or document, this method ignores most of the 512-byte header that occurs before the start of the actual picture data. It may retrieve some relevant meta information from the header.

## Parameters

- `pictData`: A data object containing the PICT data.

## See Also

### Related Documentation
- [var pictRepresentation: Data](./pictrepresentation.md)
  The image representation’s PICT data.
- [+ imageRepWithData:](./imagerepwithdata_.md)
  Creates and returns a representation of an image from the specified data in the PICT file format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspictimagerep/init(data:))*