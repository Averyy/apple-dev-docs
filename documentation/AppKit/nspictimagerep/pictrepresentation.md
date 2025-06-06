# pictRepresentation

**Framework**: AppKit  
**Kind**: property

The image representation’s PICT data.

**Availability**:
- macOS ?+

## Declaration

```swift
var pictRepresentation: Data { get }
```

#### Discussion

The data does not include the 512-byte header, if it was present in the original data. If you want to write the data to a file, you must precede it with a 512-byte header (containing all zeros) if you want to conform to the PICT document format.

## See Also

- [var boundingBox: NSRect](nspictimagerep/boundingbox.md)
  The rectangle that bounds the image representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspictimagerep/pictrepresentation)*