# Search attribute keys and values

**Framework**: Security

Filter a keychain item search.

#### Overview

When looking for items using any of the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md), [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md), or [`SecItemDelete(_:)`](secitemdelete(_:).md) functions, you specify a `query` dictionary containing both the item attributes to look for (see [`Item attribute keys and values`](item-attribute-keys-and-values.md)) and additional search attributes that condition the search. For example, you can use the matching key [`kSecMatchLimit`](ksecmatchlimit.md) with value [`kSecMatchLimitOne`](ksecmatchlimitone.md) to restrict the output to include only the first result even when more than one item matches.

## Topics

### Item search matching keys
- [let kSecMatchPolicy: CFString](ksecmatchpolicy.md)
  A key whose value indicates a policy with which a matching certificate or identity must verify.
- [let kSecMatchItemList: CFString](ksecmatchitemlist.md)
  A key whose value indicates a list of items to search.
- [let kSecMatchSearchList: CFString](ksecmatchsearchlist.md)
  A key whose value indicates a list of items to search.
- [let kSecMatchIssuers: CFString](ksecmatchissuers.md)
  A key whose value is a string to match against a certificate or identity’s issuers.
- [let kSecMatchEmailAddressIfPresent: CFString](ksecmatchemailaddressifpresent.md)
  A key whose value is a string to match against a certificate or identity’s email address.
- [let kSecMatchSubjectContains: CFString](ksecmatchsubjectcontains.md)
  A key whose value is a string to look for in a certificate or identity’s subject.
- [let kSecMatchSubjectStartsWith: CFString](ksecmatchsubjectstartswith.md)
  A key whose value is a string to match against the beginning of a certificate or identity’s subject.
- [let kSecMatchSubjectEndsWith: CFString](ksecmatchsubjectendswith.md)
  A key whose value is a string to match against the end of a certificate or identity’s subject.
- [let kSecMatchSubjectWholeString: CFString](ksecmatchsubjectwholestring.md)
  A key whose value is a string to exactly match a certificate or identity’s subject.
- [let kSecMatchCaseInsensitive: CFString](ksecmatchcaseinsensitive.md)
  A key whose value is a Boolean indicating whether case-insensitive matching is performed.
- [let kSecMatchDiacriticInsensitive: CFString](ksecmatchdiacriticinsensitive.md)
  A key whose value is a Boolean indicating whether diacritic-insensitive matching is performed.
- [let kSecMatchWidthInsensitive: CFString](ksecmatchwidthinsensitive.md)
  A key whose value is a Boolean indicating whether width-insensitive matching is performed.
- [let kSecMatchTrustedOnly: CFString](ksecmatchtrustedonly.md)
  A key whose value is a Boolean indicating whether untrusted certificates should be returned.
- [let kSecMatchValidOnDate: CFString](ksecmatchvalidondate.md)
  A key whose value indicates the validity date.
- [let kSecMatchLimit: CFString](ksecmatchlimit.md)
  A key whose value indicates the match limit.
### Match limit values
- [let kSecMatchLimitOne: CFString](ksecmatchlimitone.md)
  A value that corresponds to matching exactly one item.
- [let kSecMatchLimitAll: CFString](ksecmatchlimitall.md)
  A value that corresponds to matching an unlimited number of items.
### Additional item search keys
- [let kSecUseItemList: CFString](ksecuseitemlist.md)
  A key whose value is an array of items to search.
- [let kSecUseKeychain: CFString](ksecusekeychain.md)
  A key whose value is a keychain to operate on.
- [let kSecUseOperationPrompt: CFString](ksecuseoperationprompt.md)
  A key whose value is an operation prompt.
- [let kSecUseNoAuthenticationUI: CFString](ksecusenoauthenticationui.md)
  A key whose value is a Boolean indicating whether to disallow UI authentication.
- [let kSecUseAuthenticationUI: CFString](ksecuseauthenticationui.md)
  A key whose value indicates whether the user is prompted for authentication.
- [let kSecUseAuthenticationContext: CFString](ksecuseauthenticationcontext.md)
  A key whose value indicates a local authentication context to use.
- [let kSecUseDataProtectionKeychain: CFString](ksecusedataprotectionkeychain.md)
  A key whose value indicates whether to treat macOS keychain items like iOS keychain items.
### UI authentication values
- [let kSecUseAuthenticationUIAllow: CFString](ksecuseauthenticationuiallow.md)
  A value that indicates user authentication is allowed.
- [let kSecUseAuthenticationUIFail: CFString](ksecuseauthenticationuifail.md)
  A value that indicates user authentication is disallowed.
- [let kSecUseAuthenticationUISkip: CFString](ksecuseauthenticationuiskip.md)
  A value that indicates items requiring user authentication should be skipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/search-attribute-keys-and-values)*