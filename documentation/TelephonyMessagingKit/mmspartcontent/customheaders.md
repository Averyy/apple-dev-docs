# customHeaders

**Framework**: TelephonyMessagingKit  
**Kind**: property

A dictionary of custom headers to send in the MMS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var customHeaders: [MMSPartContent.MMSCustomHeader]
```

#### Discussion

Delivery of custom headers isn’t guaranteed, since delivery depends on how accurately the cellular carrier network transports the MMS content.

## See Also

- [func addCustomHeader(MMSPartContent.MMSCustomHeader)](mmspartcontent/addcustomheader(_:).md)
  A helper function to add custom headers.
- [MMSPartContent.MMSCustomHeader](mmspartcontent/mmscustomheader.md)
  A structure that defines a custom header as a key-value pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/customheaders)*