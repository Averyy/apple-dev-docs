# duration

**Framework**: App License Delivery SDK  
**Kind**: property

The maximum amount of time, in seconds, that iOS considers the license valid.

## Declaration

```swift
var duration: UInt64
```

## Mentions

- [Renewing and revoking app licenses](renewing-and-revoking-app-licenses.md)
- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)

#### Discussion

The alternative app marketplace determines a value for this property at its discretion. iOS doesn’t let an app launch if the duration of its license lapses.

A value of `0` indicates that the license doesn’t expire. To revoke a license, see [`Renewing and revoking app licenses`](renewing-and-revoking-app-licenses.md).

For an example that sets this property, see [`Licensing alternative distribution apps`](licensing-alternative-distribution-apps.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldlicenseattribute/duration)*