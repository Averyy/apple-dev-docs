# alwaysEnabled

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

A testing mode that automatically enables the domain.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
static var alwaysEnabled: NSFileProviderDomain.TestingModes { get }
```

```c
NSFileProviderDomainTestingModeAlwaysEnabled
```

#### Discussion

By default, the user must manually enable a domain in System Preferences > Extensions before the File Provider extension can access it. This testing mode bypasses that workflow and automatically enables the domain.

## See Also

### Accessing Modes
- [static var interactive: NSFileProviderDomain.TestingModes](./interactive.md)
  A testing mode where the extension can deterministically test asynchronous operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/testingmodes-swift.struct/alwaysenabled)*