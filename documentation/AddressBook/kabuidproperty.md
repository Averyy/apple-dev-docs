# kABUIDProperty

**Framework**: Address Book  
**Kind**: var  
**Role**: Global Variable

The unique ID for this record. It’s guaranteed never to change, no matter how much the record changes. If you need to store a reference to a record, use this value. Type: [`kABStringProperty`](./kabstringproperty.md).

**Availability**:
- macOS

## Declaration

```swift
let kABUIDProperty: String
```

```c
extern NSString * const kABUIDProperty;
```

## See Also

### Constants
- [let kABCreationDateProperty: String](./kabcreationdateproperty.md)
  The date when the record was first saved. Type: [`kABDateProperty`](./kabdateproperty.md).
- [let kABModificationDateProperty: String](./kabmodificationdateproperty.md)
  The date when the record was last saved. Type: [`kABDateProperty`](./kabdateproperty.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/kabuidproperty)*