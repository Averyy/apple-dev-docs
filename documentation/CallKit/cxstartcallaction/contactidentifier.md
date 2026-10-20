# contactIdentifier

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSString * contactIdentifier;
```

#### Discussion

The identifier is displayed in the native call UI, and is typically the name of the call recipient.

If a caller corresponds to a [`CNContact`](../../Contacts/cncontact.md) object, set this to the value of the [`identifier`](../../Contacts/cncontact/identifier.md) property of the contact.

## See Also

### Accessing Action Attributes
- [var isVideo: Bool](./isvideo.md)
  A Boolean value that indicates whether the call is a video call.
- [var handle: CXHandle](./handle.md)
  The handle of the call recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxstartcallaction/contactidentifier)*