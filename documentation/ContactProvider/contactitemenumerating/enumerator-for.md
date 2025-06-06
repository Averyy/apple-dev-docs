# enumerator(for:)

**Framework**: ContactProvider  
**Kind**: method  
**Required**: Yes

Provide an enumerator for the contact items collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func enumerator(for collection: ContactItem.Identifier) -> any ContactItemEnumerator
```

#### Discussion

The collection represents all contacts for the domain (`ContactItem.Identifier.rootContainer`).

## Parameters

- `collection`: The collection to enumerate; defaults to   .

## See Also

- [ContactItem.Identifier](contactitem/identifier.md)
  The app’s identifier for an item in the contact database.
- [protocol ContactItemEnumerator](contactitemenumerator.md)
  A protocol to provide enumerations of all contact items and changed contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemenumerating/enumerator(for:))*