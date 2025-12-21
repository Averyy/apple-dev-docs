# setPrimaryIdentifier(_:)

**Framework**: Address Book  
**Kind**: method

Sets the primary value to be the value for the given identifier.

**Availability**:
- macOS ?+

## Declaration

```swift
func setPrimaryIdentifier(_ identifier: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the identifier is `nil`, this method raises an exception. Use the [`identifier(at:)`](abmultivalue/identifier(at:).md) method to get the identifier given the index.

## Parameters

- `identifier`: The identifier whose value will be used as the primary value for a multivalue property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/setprimaryidentifier(_:))*