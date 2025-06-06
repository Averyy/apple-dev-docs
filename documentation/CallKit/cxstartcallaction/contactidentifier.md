# contactIdentifier

**Framework**: CallKit  
**Kind**: property

The identifier for the call recipient.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var contactIdentifier: String? { get set }
```

#### Discussion

The identifier is displayed in the native call UI, and is typically the name of the call recipient.

If a caller corresponds to a [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact) object, set this to the value of the [`identifier`](https://developer.apple.com/documentation/Contacts/CNContact/identifier) property of the contact.

## See Also

- [var isVideo: Bool](cxstartcallaction/isvideo.md)
  A Boolean value that indicates whether the call is a video call.
- [var handle: CXHandle](cxstartcallaction/handle.md)
  The handle of the call recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxstartcallaction/contactidentifier)*