# defaultValue

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The default value of the attribute.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var defaultValue: Any? { get set }
```

```objc
@property (retain, nullable) id defaultValue;
```

#### Discussion

Default values are retained by a managed object model, not copied. This means that attribute values do not have to implement the `NSCopying` protocol, however it also means that you should not modify any objects after they have been set as default values.

##### Special Considerations

Setting the default value raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Configuring the behavior
- [var allowsCloudEncryption: Bool](./allowscloudencryption.md)
  A Boolean value that determines whether to encrypt the attribute’s value.
- [var allowsExternalBinaryDataStorage: Bool](./allowsexternalbinarydatastorage.md)
  A Boolean value that indicates whether the attribute allows external binary storage.
- [var preservesValueInHistoryOnDeletion: Bool](./preservesvalueinhistoryondeletion.md)
  A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.
- [var valueTransformerName: String?](./valuetransformername.md)
  The name of the transformer to use for the attribute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/defaultvalue)*