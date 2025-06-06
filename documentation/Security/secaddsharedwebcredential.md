# SecAddSharedWebCredential(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Asynchronously stores (or updates) a shared password for a website.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func SecAddSharedWebCredential(_ fqdn: CFString, _ account: CFString, _ password: CFString?, _ completionHandler: @escaping (CFError?) -> Void)
```

## Mentions

- [Managing Shared Credentials](managing-shared-credentials.md)

#### Discussion

This function adds a shared password item that will be accessible by Safari and apps that have the specified fully qualified domain name in their [`Associated Domains Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.associated-domains). If a shared password item already exists for the specified website and account, it is updated with the provided password. To remove a password, pass `NULL` for the password parameter.

> **Note**:  Because a request involving shared web credentials may potentially require user interaction or other verification to be approved, this function is dispatched asynchronously; your code provides a completion handler that is called as soon as the results (if any) are available.

 Because a request involving shared web credentials may potentially require user interaction or other verification to be approved, this function is dispatched asynchronously; your code provides a completion handler that is called as soon as the results (if any) are available.

When this function is called, the system tries to get the site association file from the server. If the file is unavailable, the sever returns a 500-599 code.

## Parameters

- `fqdn`: The fully qualified domain name of the website requiring the password.
- `account`: The account name associated with this password.
- `password`: The password to be stored. Pass   to remove a shared password if it exists.
- `completionHandler`: The block takes one argument:


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaddsharedwebcredential(_:_:_:_:))*