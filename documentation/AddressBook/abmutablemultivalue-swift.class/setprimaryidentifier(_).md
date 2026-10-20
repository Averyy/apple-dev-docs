# setPrimaryIdentifier(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Sets the primary value to be the value for the given identifier.

**Availability**:
- macOS

## Declaration

```swift
func setPrimaryIdentifier(_ identifier: String!) -> Bool
```

```objc
- (BOOL) setPrimaryIdentifier:(NSString *) identifier;
```

#### Return Value

[`true`](../../Swift/true.md) if successful; otherwise [`false`](../../Swift/false.md).

#### Discussion

If the identifier is `nil`, this method raises an exception. Use the [`identifier(at:)`](../abmultivalue-swift.class/identifier%28at%29.md) method to get the identifier given the index.

## Parameters

- `identifier`: The identifier whose value will be used as the primary value for a multivalue property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue-swift.class/setprimaryidentifier(_:))*