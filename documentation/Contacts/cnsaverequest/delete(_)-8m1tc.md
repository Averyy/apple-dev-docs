# delete(_:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Deletes a contact from the contact store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func delete(_ contact: CNMutableContact)
```

```objc
- (void) deleteContact:(CNMutableContact *) contact;
```

## Parameters

- `contact`: Contact to be delete.

## See Also

### Saving contact changes
- [func add(CNMutableContact, toContainerWithIdentifier: String?)](./add%28_,tocontainerwithidentifier%29-7eut4.md)
  Adds the specified contact to the contact store.
- [func update(CNMutableContact)](./update%28_%29-3gaig.md)
  Updates an existing contact in the contact store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/delete(_:)-8m1tc)*