# NSUpdateDynamicServices()

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Causes the services information for the system to be updated.

**Availability**:
- macOS

## Declaration

```swift
func NSUpdateDynamicServices()
```

```c
extern void NSUpdateDynamicServices();
```

## Discussion

Used by a service-providing application to reregister the services it is willing to provide. To do this, you create a bundle with the extension “`.service`” and place it in the application’s path or `~/Library/Services`. The content of the bundle is identical to a normal service bundle. You then call this function.

It is only necessary to call this function if your program adds dynamic services to the system.

## See Also

### Registering Services
- [func NSRegisterServicesProvider(Any?, NSServiceProviderName)](./nsregisterservicesprovider%28_,_%29.md)
  Registers a service provider.
- [func NSUnregisterServicesProvider(NSServiceProviderName)](./nsunregisterservicesprovider%28_%29.md)
  Unregisters a service provider.
- [typealias NSServiceProviderName](./nsserviceprovidername.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsupdatedynamicservices())*