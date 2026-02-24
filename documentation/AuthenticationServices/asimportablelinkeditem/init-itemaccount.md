# init(item:account:)

**Framework**: Authentication Services  
**Kind**: init

Creates a linked item from the identifiers of an item and an account.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(item: Data, account: Data? = nil)
```

## Parameters

- `item`: The [`id`](asimportableitem/id.md) of the item linked by this `LinkedItem`.
- `account`: The [`id`](asimportableaccount/id.md) of the Account to which this `LinkedItem` belongs, if any. Defaults to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablelinkeditem/init(item:account:))*