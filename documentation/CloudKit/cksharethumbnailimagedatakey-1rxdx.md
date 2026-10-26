# CKShareThumbnailImageDataKey

**Framework**: CloudKit  
**Kind**: var  
**Role**: Global Variable

The system field key for the share’s thumbnail image data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern CKRecordFieldKey const CKShareThumbnailImageDataKey;
```

#### Discussion

This predefined key is part of the `CKRecordTypeShare` schema.  It is used by the out of process UI flow to send a share, and as part of the share acceptance flow.  It is an optional value on a `CKShare` record.

## See Also

### Subscripting
- [CKShareTypeKey](./cksharetypekey-204gl.md)
  The system field key for the share’s type.
- [CKShareTitleKey](./cksharetitlekey-9yavd.md)
  The system field key for the share’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharethumbnailimagedatakey-1rxdx)*