# alternateRegion

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A region that location services can monitor more effectively.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
var alternateRegion: CLRegion? { get }
```

#### Discussion

This property has a value only for errors of type [`regionMonitoringResponseDelayed`](./regionmonitoringresponsedelayed.md).

## See Also

### Getting the error details
- [static var errorDomain: String](./errordomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/alternateregion)*