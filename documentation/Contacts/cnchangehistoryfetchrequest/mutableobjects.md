# mutableObjects

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the fetch should return mutable contacts and groups.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var mutableObjects: Bool { get set }
```

```objc
@property (nonatomic) BOOL mutableObjects;
```

## Discussion

Specify [`true`](../../Swift/true.md) to receive mutable contacts and groups. Default is [`false`](../../Swift/false.md).

## See Also

### Configuring the fetch request
- [var additionalContactKeyDescriptors: [any CNKeyDescriptor]?](./additionalcontactkeydescriptors.md)
  An array of contact property keys or key descriptors from contact objects to fetch in the returned contacts.
- [var excludedTransactionAuthors: [String]?](./excludedtransactionauthors.md)
  An array of strings that identify transaction authors to exclude from the fetch results.
- [var includeGroupChanges: Bool](./includegroupchanges.md)
  A Boolean value that indicates whether the fetch should also return group changes.
- [var shouldUnifyResults: Bool](./shouldunifyresults.md)
  A Boolean value that indicates whether the fetch should return contact changes as unified contacts.
- [var startingToken: Data?](./startingtoken.md)
  An opaque token that indicates a point in history in the user’s Contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/mutableobjects)*