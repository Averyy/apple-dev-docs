# provider

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The provider servicing the request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var provider: any ASAuthorizationProvider { get }
```

```objc
@property (nonatomic, strong, readonly) id<ASAuthorizationProvider> provider;
```

## See Also

### Inspecting the Provider
- [protocol ASAuthorizationProvider](../asauthorizationprovider.md)
  An interface that authorization providers must implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationrequest/provider)*