# userInfo

**Framework**: File Provider  
**Kind**: property  
**Required**: Yes

Global state information about the current domain version.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any] { get }
```

#### Discussion

Use this dictionary to add state information to the domain. You can then access the [`userInfo`](nsfileproviderdomainstate/userinfo.md) dictionary in predicates for user interactions, file provider actions, and [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI) actions using the `domainUserInfo` context key.

This dictionary must only contain the following types for both its keys and values:

- [`NSString`](https://developer.apple.com/documentation/Foundation/NSString)
- [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber)
- [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate)
- [`NSPersonNameComponents`](https://developer.apple.com/documentation/Foundation/NSPersonNameComponents)

The system expects you to update the `domainVersion` whenever the value of the [`userInfo`](nsfileproviderdomainstate/userinfo.md) dictionary changes.

## See Also

- [var domainVersion: NSFileProviderDomainVersion](nsfileproviderdomainstate/domainversion.md)
  An opaque object that uniquely identifies the domain’s version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomainstate/userinfo)*