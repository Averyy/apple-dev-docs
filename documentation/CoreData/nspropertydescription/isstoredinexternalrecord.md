# isStoredInExternalRecord

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to write the property’s data in an external record file that corresponds to the managed object.

**Availability**:
- iOS 3.0+ - Deprecated in 11.0
- iPadOS 3.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.13
- tvOS - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Spotlight integration is deprecated. Use CoreSpotlight integration instead.

## Declaration

```swift
var isStoredInExternalRecord: Bool { get set }
```

```objc
@property (getter=isStoredInExternalRecord) BOOL storedInExternalRecord;
```

## Discussion

[`true`](../../Swift/true.md) if the property data should be written out in an external record file corresponding to the managed object, otherwise [`false`](../../Swift/false.md). For additional information, see [Core Data Spotlight Integration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpotlightCoreData/Introduction/introSpotlightCoreData.html#//apple_ref/doc/uid/TP40008065).

### Special Considerations

This property has no effect on iOS.

## See Also

### Specifying Spotlight Support
- [var isIndexedBySpotlight: Bool](./isindexedbyspotlight.md)
  A Boolean value that indicates whether Core Data adds the property’s value to the Core Spotlight index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/isstoredinexternalrecord)*