# canOpen

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether the app can open the external link account.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.4+

## Declaration

```swift
static var canOpen: Bool { get async }
```

#### Discussion

Check this property before showing any user-interface controls that enable people to open the external link account.

Don’t check this property again in response to user input; instead, call [`open()`](externallinkaccount/open().md) immediately.

> ❗ **Important**:  Only show user-interface controls that call the [`open()`](externallinkaccount/open().md) method if this property is `true`. The [`open()`](externallinkaccount/open().md) method always throws an error when [`canOpen`](externallinkaccount/canopen.md) is `false`.

 Only show user-interface controls that call the [`open()`](externallinkaccount/open().md) method if this property is `true`. The [`open()`](externallinkaccount/open().md) method always throws an error when [`canOpen`](externallinkaccount/canopen.md) is `false`.

## See Also

- [static func open() async throws](externallinkaccount/open.md)
  Presents a continuation sheet that enables people to choose whether to open your app’s link to an external website for account creation or management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externallinkaccount/canopen)*