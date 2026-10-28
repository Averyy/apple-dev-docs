# MMSPartContent.MMSCustomHeader

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that defines a custom header as a key-value pair.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct MMSCustomHeader
```

## Overview

TelephonyMessagingKit exposes custom headers in case a message needs to include them in an MMS message.

## Topics

### Accessing header properties
- [let key: String](./mmscustomheader/key.md)
  The key for the custom header.
- [let value: String](./mmscustomheader/value.md)
  The value of the custom header.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with custom headers
- [var customHeaders: [MMSPartContent.MMSCustomHeader]](./customheaders.md)
  A dictionary of custom headers to send in the MMS message.
- [func addCustomHeader(MMSPartContent.MMSCustomHeader)](./addcustomheader%28_%29.md)
  A helper function to add custom headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/mmscustomheader)*