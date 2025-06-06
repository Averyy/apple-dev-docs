# LSMinimumSystemVersion

**Framework**: Bundle Resources  
**Kind**: typealias

The minimum version of the operating system required for the app to run in macOS.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

#### Discussion

Use this key to indicate the minimum macOS release that your app supports. The App Store uses this key to indicate the macOS releases on which your app can run, and to show compatibility with a person’s Mac.

Starting with macOS 11.4, the lowest version number you can specify as the value for the [`LSMinimumSystemVersion`](information-property-list/lsminimumsystemversion.md) key is:

- `10` if your app links against the macOS SDK.
- `10.15` if your app links against the iOS 14.3 SDK (or later) and builds using Mac Catalyst.
- `11` if your iPad or iPhone app links against the iOS 14.3 SDK (or later) and can run on a Mac with Apple silicon.

To specify the minimum version of iOS, iPadOS, tvOS, or watchOS that your app supports, use [`MinimumOSVersion`](information-property-list/minimumosversion.md).

## See Also

- [LSMinimumSystemVersionByArchitecture](information-property-list/lsminimumsystemversionbyarchitecture.md)
  The minimum version of macOS required for the app to run on a set of architectures.
- [MinimumOSVersion](information-property-list/minimumosversion.md)
  The minimum version of the operating system required for the app to run in iOS, iPadOS, tvOS, and watchOS.
- [LSRequiresIPhoneOS](information-property-list/lsrequiresiphoneos.md)
  A Boolean value indicating whether the app must run in iOS.
- [WKApplication](information-property-list/wkapplication.md)
- [WKWatchKitApp](information-property-list/wkwatchkitapp.md)
  A Boolean value that indicates whether the bundle is a watchOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/lsminimumsystemversion)*