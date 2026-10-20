# customHeaders

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

A dictionary of custom headers to send in the MMS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var customHeaders: [MMSPartContent.MMSCustomHeader]
```

#### Discussion

Delivery of custom headers isn’t guaranteed, since delivery depends on how accurately the cellular carrier network transports the MMS content.

## See Also

### Working with custom headers
- [func addCustomHeader(MMSPartContent.MMSCustomHeader)](./addcustomheader%28_%29.md)
  A helper function to add custom headers.
- [MMSPartContent.MMSCustomHeader](./mmscustomheader.md)
  A structure that defines a custom header as a key-value pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/customheaders)*