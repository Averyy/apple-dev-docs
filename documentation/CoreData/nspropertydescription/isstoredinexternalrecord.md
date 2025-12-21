# isStoredInExternalRecord

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether to write the property’s data in an external record file that corresponds to the managed object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isStoredInExternalRecord: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the property data should be written out in an external record file corresponding to the managed object, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). For additional information, see [`Core Data Spotlight Integration Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpotlightCoreData/Introduction/introSpotlightCoreData.html#//apple_ref/doc/uid/TP40008065).

##### Special Considerations

This property has no effect on iOS.

## See Also

- [var isIndexedBySpotlight: Bool](nspropertydescription/isindexedbyspotlight.md)
  A Boolean value that indicates whether Core Data adds the property’s value to the Core Spotlight index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/isstoredinexternalrecord)*