# extraAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A dictionary of additional attributes for a metadata item.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`extraAttributes`](../avpartialasyncproperty/extraattributes.md) asynchronously instead.

## Declaration

```swift
var extraAttributes: [AVMetadataExtraAttributeKey : Any]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDictionary<NSString *,id> * extraAttributes;
```

#### Discussion

Extra attributes, when they’re present, are specific to metadata container formats and keys in their associated key-spaces. For example, a metadata item can represent the “attached picture” frame defined by the ID3 tag specification with keyspace [`id3`](../avmetadatakeyspace/id3.md) and key [`id3MetadataKeyAttachedPicture`](../avmetadatakey/id3metadatakeyattachedpicture.md), a value that carries the image data, and extra attributes that include a description of the picture as carried in the ‘APIC’ frame of the ID3 tag.

## See Also

### Accessing values
- [var value: (any NSCopying & NSObjectProtocol)?](./value.md)
  The value of the metadata item.
- [var stringValue: String?](./stringvalue.md)
  The value of the metadata item as a string.
- [var numberValue: NSNumber?](./numbervalue.md)
  The value of the metadata item as a number.
- [var dateValue: Date?](./datevalue.md)
  The value of the metadata item as a date.
- [var dataValue: Data?](./datavalue.md)
  The value of the metadata item as a data value.
- [- loadValuesAsynchronouslyForKeys:completionHandler:](./loadvaluesasynchronouslyforkeys_completionhandler_.md)
  Tells the object to load the values of any of the specified keys that aren’t already loaded.
- [- statusOfValueForKey:error:](./statusofvalueforkey_error_.md)
  Reports whether the value for a given key is immediately available without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/extraattributes)*