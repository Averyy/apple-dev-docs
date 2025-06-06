# versionHash

**Framework**: Core Data  
**Kind**: property

The version hash for the attribute.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var versionHash: Data { get }
```

#### Discussion

The version hash is used to uniquely identify an attribute based on its configuration. This value includes the [`versionHash`](nspropertydescription/versionhash.md) information from [`NSPropertyDescription`](nspropertydescription.md) and the attribute type.

## See Also

- [var versionHash: Data](nspropertydescription/versionhash.md)
  The version hash for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/versionhash)*