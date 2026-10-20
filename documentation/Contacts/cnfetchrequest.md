# CNFetchRequest

**Framework**: Contacts  
**Kind**: class  
**Role**: Class

The base class for contact fetch requests.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNFetchRequest
```

```objc
@interface CNFetchRequest : NSObject
```

#### Overview

To fetch contacts, use [`CNContactFetchRequest`](./cncontactfetchrequest.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CNChangeHistoryFetchRequest](./cnchangehistoryfetchrequest.md)
- [CNContactFetchRequest](./cncontactfetchrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Fetch and save requests
- [class CNContactFetchRequest](./cncontactfetchrequest.md)
  An object that defines the options to use when fetching contacts.
- [class CNFetchResult](./cnfetchresult.md)
  An object that represents the result of a change-history fetch request.
- [class CNSaveRequest](./cnsaverequest.md)
  An object that collects the changes you want to save to the user’s contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnfetchrequest)*