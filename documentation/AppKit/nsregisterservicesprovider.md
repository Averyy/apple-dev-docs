# NSRegisterServicesProvider(_:_:)

**Framework**: AppKit  
**Kind**: func

Registers a service provider.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSRegisterServicesProvider(_ provider: Any?, _ name: NSServiceProviderName)
```

#### Discussion

Use this function to register custom services not directly related to your application.

You should not use this function to register the services provided by your application. For your application’s services, you should use the [`servicesProvider`](nsapplication/servicesprovider.md) method of [`NSApplication`](nsapplication.md), passing a non-`nil` argument.

## Parameters

- `provider`: The object providing the service you want to register.
- `name`: The unique name to associate with the service. This string is used to advertise the service to interested clients.

## See Also

- [func NSUnregisterServicesProvider(NSServiceProviderName)](nsunregisterservicesprovider(_:).md)
  Unregisters a service provider.
- [func NSUpdateDynamicServices()](nsupdatedynamicservices().md)
  Causes the services information for the system to be updated.
- [typealias NSServiceProviderName](nsserviceprovidername.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsregisterservicesprovider(_:_:))*