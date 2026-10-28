# canOpen

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

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

## Discussion

Check this property before showing any user-interface controls that enable people to open the external link account.

Don’t check this property again in response to user input; instead, call [`open()`](./open%28%29.md) immediately.

> ❗ **Important**:  Only show user-interface controls that call the [`open()`](./open%28%29.md) method if this property is `true`. The [`open()`](./open%28%29.md) method always throws an error when [`canOpen`](./canopen.md) is `false`.

## See Also

### Linking to external accounts
- [static func open() async throws](./open%28%29.md)
  Presents a continuation sheet that enables people to choose whether to open your app’s link to an external website for account creation or management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externallinkaccount/canopen)*