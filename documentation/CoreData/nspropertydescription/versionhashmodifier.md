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

This value is included in the version hash for the property. You use it to mark or denote a property as being a different “version” than another even if all of the values which affect persistence are equal. (Such a difference is important in cases where the attributes of a property are unchanged but the format or content of its data are changed.)

## See Also

- [var versionHash: Data](nspropertydescription/versionhash.md)
  The version hash for the receiver.
- [var renamingIdentifier: String?](nspropertydescription/renamingidentifier.md)
  The renaming identifier for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/versionhashmodifier)*