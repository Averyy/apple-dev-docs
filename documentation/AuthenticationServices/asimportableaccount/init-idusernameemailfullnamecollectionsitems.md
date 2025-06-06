# init(id:userName:email:fullName:collections:items:)

**Framework**: Authentication Services  
**Kind**: init

Creates an account instance from its required and optional properties.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
init(id: Data, userName: String, email: String, fullName: String? = nil, collections: [ASImportableCollection], items: [ASImportableItem])
```

## Parameters

- `id`: A unique identifier for the account.
- `userName`: The username associated with the account.
- `email`: The email address associated with the account.
- `fullName`: The full name of the account owner, if provided.
- `collections`: An array of   instances to store in the account.
- `items`: An array of   instances to store in the account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableaccount/init(id:username:email:fullname:collections:items:))*