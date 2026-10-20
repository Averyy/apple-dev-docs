# containerIdentifier

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

A string that uniquely identifies the container where the user added the contact.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var containerIdentifier: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * containerIdentifier;
```

## See Also

### Getting event details
- [var contact: CNContact](./contact.md)
  The contact the user added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryaddcontactevent/containeridentifier)*