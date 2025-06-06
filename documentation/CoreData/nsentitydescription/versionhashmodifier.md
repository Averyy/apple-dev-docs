# versionHashModifier

**Framework**: Core Data  
**Kind**: property

The version hash modifier for the receiver.

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
var versionHashModifier: String? { get set }
```

#### Discussion

This value is included in the version hash for the entity. You use it to mark or denote an entity as being a different “version” than another even if all of the values which affect persistence are equal. (Such a difference is important in cases where, for example, the structure of an entity is unchanged but the format or content of data has changed.)

## See Also

- [var versionHash: Data](nsentitydescription/versionhash.md)
  The version hash for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/versionhashmodifier)*