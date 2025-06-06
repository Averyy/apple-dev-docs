# OSBundleCompatibleVersion

**Framework**: Bundle Resources  
**Kind**: typealias

The backward limit of compatibility for the current driver.

**Availability**:
- macOS 10.0+

#### Discussion

Specify a previous version for the current driver, or the driver’s current version. Format this string the same way you format the value of the [`CFBundleVersion`](information-property-list/cfbundleversion.md) key. The combination of this value and the value in the [`CFBundleVersion`](information-property-list/cfbundleversion.md) key define the range of versions that offers the same level of compatibility. Dependent drivers use this information to determine if they are compatible with the driver. For example, if the driver’s current version is `10.0`, and you set the value of this key to `5.0`, a driver that depends on version `7.0` can successfully use the current driver.

When you change your driver in a way that breaks compatibility with your old code, update the value of this key. At that time, set the new value to the current version of your driver.

## See Also

- [OSBundleLibraries](information-property-list/osbundlelibraries.md)
  The drivers that the system must load before your driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/osbundlecompatibleversion)*