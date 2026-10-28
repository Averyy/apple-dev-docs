# domainVersion

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The domain version when the system last refreshed the pending set.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var domainVersion: NSFileProviderDomainVersion? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSFileProviderDomainVersion * domainVersion;
```

## Discussion

The system sets this property when you call the enumerator’s methods. The value is initially `nil`.

## See Also

### Accessing Refresh Data
- [var refreshInterval: TimeInterval](./refreshinterval.md)
  The amount of time, in seconds, between updates to the pending set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderpendingsetenumerator/domainversion)*