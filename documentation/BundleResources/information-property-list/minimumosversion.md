# MinimumOSVersion

**Framework**: Bundle Resources  
**Kind**: typealias

The minimum version of the operating system required for the app to run in iOS, iPadOS, tvOS, and watchOS.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Mentions

- [Managing Your App’s Information Property List](managing-your-app-s-information-property-list.md)

#### Discussion

The App Store uses this key to indicate the OS releases on which your app can run.

Don’t specify `MinimumOSVersion` in the `Info.plist` file for apps built in Xcode. It uses the value of the Deployment Target in the General settings pane.

For macOS, see [`LSMinimumSystemVersion`](information-property-list/lsminimumsystemversion.md).

## See Also

- [LSMinimumSystemVersion](information-property-list/lsminimumsystemversion.md)
  The minimum version of the operating system required for the app to run in macOS.
- [LSMinimumSystemVersionByArchitecture](information-property-list/lsminimumsystemversionbyarchitecture.md)
  The minimum version of macOS required for the app to run on a set of architectures.
- [LSRequiresIPhoneOS](information-property-list/lsrequiresiphoneos.md)
  A Boolean value indicating whether the app must run in iOS.
- [WKApplication](information-property-list/wkapplication.md)
- [WKWatchKitApp](information-property-list/wkwatchkitapp.md)
  A Boolean value that indicates whether the bundle is a watchOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/minimumosversion)*