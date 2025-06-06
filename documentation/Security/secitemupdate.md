# SecItemUpdate(_:_:)

**Framework**: Security  
**Kind**: func

Modifies items that match a search query.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecItemUpdate(_ query: CFDictionary, _ attributesToUpdate: CFDictionary) -> OSStatus
```

## Mentions

- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The query dictionary for update can’t contain [`Item return result keys`](item-return-result-keys.md), because [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md) only returns a status.

##### Performance Considerations

`SecItemUpdate` blocks the calling thread, so it can cause your app’s UI to hang if called from the main thread. Instead, call `SecItemUpdate` from a background dispatch queue or `async` function:

## Parameters

- `query`: A dictionary that describes the search for the keychain items you want to update. A typical   dictionary consists of:
- `attributesToUpdate`: A dictionary containing the attributes whose values should update, along with the new values. Only real keychain attributes are permitted in this dictionary (no “meta” attributes are allowed.) For the attributes applicable to the keychain item you’re updating, see the entry for the item’s class in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemupdate(_:_:))*