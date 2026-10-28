# sharedContainerIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The identifier for the shared container into which files in background URL sessions should be downloaded.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sharedContainerIdentifier: String? { get set }
```

```objc
@property (copy, nullable) NSString * sharedContainerIdentifier;
```

## Discussion

To create a URL session for use by an app extension, set this property to a valid identifier for a container shared between the app extension and its containing app.

> ❗ **Important**:  If you try to create a URL session from your app extension but fail to set this property to a valid value, the URL session is invalidated upon creation.

For information about app extensions, see [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## See Also

### Related Documentation
- [var NSURLErrorBackgroundSessionRequiresSharedContainer: Int](../nsurlerrorbackgroundsessionrequiressharedcontainer-swift.var.md)
  The shared container identifier of the URL session configuration is needed but hasn’t been set.
- [NSURLErrorBackgroundSessionRequiresSharedContainer](../nsurlerrorbackgroundsessionrequiressharedcontainer-c.enum.case.md)
  The shared container identifier of the URL session configuration is needed but hasn’t been set.
### Setting general properties
- [var identifier: String?](./identifier.md)
  The background session identifier of the configuration object.
- [var httpAdditionalHeaders: [AnyHashable : Any]?](./httpadditionalheaders.md)
  A dictionary of additional headers to send with requests.
- [var networkServiceType: NSURLRequest.NetworkServiceType](./networkservicetype.md)
  The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that determines whether connections should be made over a cellular network.
- [var timeoutIntervalForRequest: TimeInterval](./timeoutintervalforrequest.md)
  The timeout interval to use when waiting for additional data.
- [var timeoutIntervalForResource: TimeInterval](./timeoutintervalforresource.md)
  The maximum amount of time that a resource request should be allowed to take.
- [var waitsForConnectivity: Bool](./waitsforconnectivity.md)
  A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
- [var usesClassicLoadingMode: Bool](./usesclassicloadingmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/sharedcontaineridentifier)*