# preservesValueInHistoryOnDeletion

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var preservesValueInHistoryOnDeletion: Bool { get set }
```

```objc
@property BOOL preservesValueInHistoryOnDeletion;
```

## See Also

### Configuring the behavior
- [var allowsCloudEncryption: Bool](./allowscloudencryption.md)
  A Boolean value that determines whether to encrypt the attribute’s value.
- [var allowsExternalBinaryDataStorage: Bool](./allowsexternalbinarydatastorage.md)
  A Boolean value that indicates whether the attribute allows external binary storage.
- [var defaultValue: Any?](./defaultvalue.md)
  The default value of the attribute.
- [var valueTransformerName: String?](./valuetransformername.md)
  The name of the transformer to use for the attribute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/preservesvalueinhistoryondeletion)*