# creationDate

**Framework**: AVFoundation  
**Kind**: property

A metadata item that indicates the asset’s creation date.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
var creationDate: AVMetadataItem? { get }
```

#### Discussion

If the asset contains metadata that the framework can convert to an [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), you can retrieve it from the metadata item using its [`dateValue`](avmetadataitem/datevalue.md) property. Otherwise, you retrieve it as a string by using the metadata item’s [`stringValue`](avmetadataitem/stringvalue.md) property.

This property value is `nil` if no creation date metadata exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/creationdate)*