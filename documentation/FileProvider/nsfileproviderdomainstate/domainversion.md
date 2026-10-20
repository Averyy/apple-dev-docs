# domainVersion

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An opaque object that uniquely identifies the domain’s version.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var domainVersion: NSFileProviderDomainVersion { get }
```

```objc
@property (nonatomic, readonly) NSFileProviderDomainVersion * domainVersion;
```

## See Also

### Accessing State Data
- [var userInfo: [AnyHashable : Any]](./userinfo.md)
  Global state information about the current domain version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomainstate/domainversion)*