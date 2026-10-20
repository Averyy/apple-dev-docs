# NSUnregisterServicesProvider(_:)

**Framework**: AppKit  
**Kind**: func

Unregisters a service provider.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSUnregisterServicesProvider(_ name: NSServiceProviderName)
```

#### Discussion

Use this function to unregister custom services not directly related to your application.

You should not use this function to unregister the services provided by your application. For your application’s services, you should use the [`servicesProvider`](nsapplication/servicesprovider.md) method of [`NSApplication`](nsapplication.md), passing a `nil` argument.

## Parameters

- `name`: The name of the service you want to unregister.

## See Also

- [func NSRegisterServicesProvider(Any?, NSServiceProviderName)](nsregisterservicesprovider(_:_:).md)
  Registers a service provider.
- [func NSUpdateDynamicServices()](nsupdatedynamicservices().md)
  Causes the services information for the system to be updated.
- [typealias NSServiceProviderName](nsserviceprovidername.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsunregisterservicesprovider(_:))*