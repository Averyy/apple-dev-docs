# LSMinimumSystemVersionByArchitecture

**Framework**: Bundle Resources  
**Kind**: dictionary

The minimum version of macOS required for the app to run on a set of architectures.

**Availability**:
- macOS 10.0+

#### Discussion

The possible dictionary keys are: `i386`, `ppc`, `ppc64`, and `x86_64`. The values are the minimum version for the architecture. The default values are `10.0.0`.

## See Also

- [LSMinimumSystemVersion](information-property-list/lsminimumsystemversion.md)
  The minimum version of the operating system required for the app to run in macOS.
- [MinimumOSVersion](information-property-list/minimumosversion.md)
  The minimum version of the operating system required for the app to run in iOS, iPadOS, tvOS, and watchOS.
- [LSRequiresIPhoneOS](information-property-list/lsrequiresiphoneos.md)
  A Boolean value indicating whether the app must run in iOS.
- [WKApplication](information-property-list/wkapplication.md)
- [WKWatchKitApp](information-property-list/wkwatchkitapp.md)
  A Boolean value that indicates whether the bundle is a watchOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/lsminimumsystemversionbyarchitecture)*