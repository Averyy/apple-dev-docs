# SecRequestSharedWebCredential(_:_:_:)

**Framework**: Security  
**Kind**: func

Asynchronously obtains one or more shared passwords for a website.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func SecRequestSharedWebCredential(_ fqdn: CFString?, _ account: CFString?, _ completionHandler: @escaping (CFArray?, CFError?) -> Void)
```

## Mentions

- [Managing Shared Credentials](managing-shared-credentials.md)

#### Discussion

This function requests one or more shared passwords for a given website, depending on whether the optional account parameter is supplied. To obtain results, the website specified in the `fqdn` parameter must be one that matches an entry in the calling app’s [`Associated Domains Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.associated-domains).

If matching shared password items are found, the credentials provided to the completion handler will be a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) data type containing [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) entries. Each dictionary contains the following pairs:

| Key | Value |
| --- | --- |
| [`kSecAttrServer`](ksecattrserver.md) | [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) (the website) |
| [`kSecAttrAccount`](ksecattraccount.md) | [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) (the account) |
| [`kSecSharedPassword`](ksecsharedpassword.md) | [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) (the password) |

If the found item specifies a nonstandard port number (other than 443 for `https`), the following key may also be present:

| [`kSecAttrPort`](ksecattrport.md) | [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) (the port number) |
| --- | --- |

> **Note**:  Because a request involving shared web credentials may potentially require user interaction or other verification to be approved, this function is dispatched asynchronously; your code provides a completion handler that will be called as soon as the results (if any) are available.

## Parameters

- `fqdn`: (Optional) The fully qualified domain name of the website for which passwords are being requested. If   is passed in this argument, the domain name(s) listed in the calling app’s   are searched implicitly.
- `account`: (Optional) The account name for which passwords are being requested. The account may be   to request all of the shared credentials that are available for the site, allowing the caller to discover an existing account.
- `completionHandler`: The block takes two arguments:


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequestsharedwebcredential(_:_:_:))*