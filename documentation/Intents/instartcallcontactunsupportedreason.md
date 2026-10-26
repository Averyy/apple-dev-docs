# INStartCallContactUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the reason the app can’t support starting a call with the contact.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INStartCallContactUnsupportedReason
```

```c
enum INStartCallContactUnsupportedReason : NSInteger;
```

## Topics

### Constants
- [INStartCallContactUnsupportedReason.noContactFound](./instartcallcontactunsupportedreason/nocontactfound.md)
  The contact wasn’t found in the app.
- [INStartCallContactUnsupportedReason.multipleContactsUnsupported](./instartcallcontactunsupportedreason/multiplecontactsunsupported.md)
  The app doesn’t support calls with multiple contacts.
- [INStartCallContactUnsupportedReason.noHandleForLabel](./instartcallcontactunsupportedreason/nohandleforlabel.md)
  The handle for the label wasn’t found.
- [INStartCallContactUnsupportedReason.invalidHandle](./instartcallcontactunsupportedreason/invalidhandle.md)
  The handle is invalid.
- [INStartCallContactUnsupportedReason.unsupportedMmiUssd](./instartcallcontactunsupportedreason/unsupportedmmiussd.md)
  An unsupported MMI codewas used.
- [INStartCallContactUnsupportedReason.noCallHistoryForRedial](./instartcallcontactunsupportedreason/nocallhistoryforredial.md)
  No redial attempt doesn’t have an associated call history.
- [INStartCallContactUnsupportedReason.noUsableHandleForRedial](./instartcallcontactunsupportedreason/nousablehandleforredial.md)
  The redial attempt doesn’t have a usable handle.
### Enumeration Cases
- [INStartCallContactUnsupportedReason.requiringInAppAuthentication](./instartcallcontactunsupportedreason/requiringinappauthentication.md)
### Initializers
- [init?(rawValue: Int)](./instartcallcontactunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result Object
- [init(personResolutionResult: INPersonResolutionResult)](./instartcallcontactresolutionresult/init%28personresolutionresult%29.md)
  Creates an object whose resolution involves the succesful start of a call with the specified contact.
- [class func unsupported(forReason: INStartCallContactUnsupportedReason) -> Self](./instartcallcontactresolutionresult/unsupported%28forreason%29.md)
  Creates an object specifying that resolution of the parameter wasn’t supported, for the specified reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcontactunsupportedreason)*