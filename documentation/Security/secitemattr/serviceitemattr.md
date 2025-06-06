# SecItemAttr.serviceItemAttr

**Framework**: Security  
**Kind**: case

Identifies the service attribute.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case serviceItemAttr
```

#### Discussion

You use this tag to set or get a string that represents the service associated with this item, for example, “iTools”. This is unique to generic password attributes. Keychain strings should use UTF-8 encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemattr/serviceitemattr)*