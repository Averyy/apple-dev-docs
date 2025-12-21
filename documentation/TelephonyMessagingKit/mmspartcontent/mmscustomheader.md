# MMSPartContent.MMSCustomHeader

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that defines a custom header as a key-value pair.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct MMSCustomHeader
```

#### Overview

TelephonyMessagingKit exposes custom headers in case a message needs to include them in an MMS message.

## Topics

### Accessing header properties
- [let key: String](mmspartcontent/mmscustomheader/key.md)
  The key for the custom header.
- [let value: String](mmspartcontent/mmscustomheader/value.md)
  The value of the custom header.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var customHeaders: [MMSPartContent.MMSCustomHeader]](mmspartcontent/customheaders.md)
  A dictionary of custom headers to send in the MMS message.
- [func addCustomHeader(MMSPartContent.MMSCustomHeader)](mmspartcontent/addcustomheader(_:).md)
  A helper function to add custom headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/mmscustomheader)*