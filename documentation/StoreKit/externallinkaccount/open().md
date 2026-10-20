# open()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents a continuation sheet that enables people to choose whether to open your app’s link to an external website for account creation or management.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.4+

## Declaration

```swift
static func open() async throws
```

#### Discussion

Call this method in response to deliberate user interaction, for example, tapping a button. Call [`canOpen`](./canopen.md) to determine whether to display a button or other user-interface control. If [`canOpen`](./canopen.md) is `false`, this method always throws a [`StoreKitError`](../storekiterror.md) instance.

## See Also

### Linking to external accounts
- [static var canOpen: Bool](./canopen.md)
  A Boolean value that indicates whether the app can open the external link account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externallinkaccount/open())*