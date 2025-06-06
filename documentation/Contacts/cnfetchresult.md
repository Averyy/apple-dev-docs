# CNFetchResult

**Framework**: Contacts  
**Kind**: class

An object that represents the result of a change-history fetch request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CNFetchResult<ValueType> where ValueType : AnyObject
```

## Topics

### Accessing results
- [var currentHistoryToken: Data](cnfetchresult/currenthistorytoken.md)
  An opaque token that indicates a point in history in the user’s Contacts database.
- [var value: ValueType](cnfetchresult/value.md)
  The result of the fetch request, expressed as the value type you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CNContactFetchRequest](cncontactfetchrequest.md)
  An object that defines the options to use when fetching contacts.
- [class CNFetchRequest](cnfetchrequest.md)
  The base class for contact fetch requests.
- [class CNSaveRequest](cnsaverequest.md)
  An object that collects the changes you want to save to the user’s contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnfetchresult)*