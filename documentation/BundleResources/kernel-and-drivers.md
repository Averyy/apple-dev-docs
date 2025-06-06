# Kernel and drivers

**Framework**: Bundle Resources

Configure device drivers provided by the app.

## Topics

### Driver personalities
- [IOKitPersonalities](information-property-list/iokitpersonalities.md)
  One or more groups of attributes that tell the system about the devices your driver supports.
### Kext dependencies
- [OSBundleCompatibleVersion](information-property-list/osbundlecompatibleversion.md)
  The backward limit of compatibility for the current driver.
- [OSBundleLibraries](information-property-list/osbundlelibraries.md)
  The drivers that the system must load before your driver.
### Thunderbolt compatibility
- [IOPCITunnelCompatible](information-property-list/iopcitunnelcompatible.md)
  A Boolean value that indicates whether your driver supports Thunderbolt devices.

## See Also

- [Protected resources](protected-resources.md)
  Control an app’s access to protected system services and user data.
- [Data and storage](data-and-storage.md)
  Regulate documents, URLs, and other kinds of data movement and storage.
- [App services](app-services.md)
  Configure services provided by the app, like support for giving directions or using game controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/kernel-and-drivers)*