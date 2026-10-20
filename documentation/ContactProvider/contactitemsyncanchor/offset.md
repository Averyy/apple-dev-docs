# offset

**Framework**: ContactProvider  
**Kind**: property  
**Role**: Instance Property

An offset from the anchor’s generation marker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var offset: Int
```

#### Discussion

You can use the offset to track a contiguous number of contact items you’ve successfully enumerated within the database generation.

## See Also

### Inspecting sync anchor properties
- [var generationMarker: Data](./generationmarker.md)
  A value specific to your data source identifying the database generation you’re enumerating for changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemsyncanchor/offset)*