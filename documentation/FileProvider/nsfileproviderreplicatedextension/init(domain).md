# init(domain:)

**Framework**: File Provider  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

Creates an instance of the file provider for the specified domain.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(domain: NSFileProviderDomain)
```

```objc
- (instancetype) initWithDomain:(NSFileProviderDomain *) domain;
```

## Parameters

- `domain`: The domain for the file provider.

## See Also

### Creating and Removing File Providers
- [func invalidate()](./invalidate%28%29.md)
  Tells the file provider to perform any necessary cleanup so that the system can deallocate it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/init(domain:))*