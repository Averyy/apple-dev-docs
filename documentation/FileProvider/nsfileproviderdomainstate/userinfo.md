# userInfo

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Global state information about the current domain version.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any] { get }
```

```objc
@property (nonatomic, strong, readonly, nonnull) NSDictionary * userInfo;
```

#### Discussion

Use this dictionary to add state information to the domain. You can then access the [`userInfo`](./userinfo.md) dictionary in predicates for user interactions, file provider actions, and [File Provider UI](../../FileProviderUI/FileProviderUI.md) actions using the `domainUserInfo` context key.

This dictionary must only contain the following types for both its keys and values:

- [`NSString`](../../Foundation/nsstring.md)
- [`NSNumber`](../../Foundation/nsnumber.md)
- [`NSDate`](../../Foundation/nsdate.md)
- [`NSPersonNameComponents`](../../Foundation/nspersonnamecomponents.md)

The system expects you to update the `domainVersion` whenever the value of the [`userInfo`](./userinfo.md) dictionary changes.

## See Also

### Accessing State Data
- [var domainVersion: NSFileProviderDomainVersion](./domainversion.md)
  An opaque object that uniquely identifies the domain’s version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomainstate/userinfo)*