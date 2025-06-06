# valueTransformerName

**Framework**: Core Data  
**Kind**: property

The name of the transformer to use for the attribute value.

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
var valueTransformerName: String? { get set }
```

#### Discussion

The attribute must be of type `NSTransformedAttributeType`.

The transformer must output an `NSData` object from [`transformedValue(_:)`](https://developer.apple.com/documentation/foundation/valuetransformer/1402004-transformedvalue) and must allow reverse transformations.

If this value is `nil`, Core Data uses a default a transformer that uses [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) to archive and unarchive the attribute value.

## See Also

- [var allowsCloudEncryption: Bool](nsattributedescription/allowscloudencryption.md)
  A Boolean value that determines whether to encrypt the attribute’s value.
- [var allowsExternalBinaryDataStorage: Bool](nsattributedescription/allowsexternalbinarydatastorage.md)
  A Boolean value that indicates whether the attribute allows external binary storage.
- [var defaultValue: Any?](nsattributedescription/defaultvalue.md)
  The default value of the attribute.
- [var preservesValueInHistoryOnDeletion: Bool](nsattributedescription/preservesvalueinhistoryondeletion.md)
  A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/valuetransformername)*