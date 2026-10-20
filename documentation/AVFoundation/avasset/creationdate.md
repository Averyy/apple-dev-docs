# creationDate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A metadata item that indicates the asset’s creation date.

**Availability**:
- iOS 5.0+ - Deprecated in 16.0
- iPadOS 5.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`creationDate`](../avpartialasyncproperty/creationdate.md) asynchronously instead.

## Declaration

```swift
var creationDate: AVMetadataItem? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVMetadataItem * creationDate;
```

#### Discussion

If the asset contains metadata that the framework can convert to an [`NSDate`](../../Foundation/nsdate.md), you can retrieve it from the metadata item using its [`dateValue`](../avmetadataitem/datevalue.md) property. Otherwise, you retrieve it as a string by using the metadata item’s [`stringValue`](../avmetadataitem/stringvalue.md) property.

This property value is `nil` if no creation date metadata exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/creationdate)*