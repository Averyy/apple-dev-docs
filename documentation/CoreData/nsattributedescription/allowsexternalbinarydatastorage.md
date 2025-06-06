# allowsExternalBinaryDataStorage

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the attribute allows external binary storage.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var allowsExternalBinaryDataStorage: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the attribute allows external binary storage, otherwise [`false`](https://developer.apple.com/documentation/swift/false). If this value is [`true`](https://developer.apple.com/documentation/swift/true), the corresponding attribute may be stored in a file external to the persistent store itself.

## See Also

- [var allowsCloudEncryption: Bool](nsattributedescription/allowscloudencryption.md)
  A Boolean value that determines whether to encrypt the attribute’s value.
- [var defaultValue: Any?](nsattributedescription/defaultvalue.md)
  The default value of the attribute.
- [var preservesValueInHistoryOnDeletion: Bool](nsattributedescription/preservesvalueinhistoryondeletion.md)
  A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.
- [var valueTransformerName: String?](nsattributedescription/valuetransformername.md)
  The name of the transformer to use for the attribute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/allowsexternalbinarydatastorage)*