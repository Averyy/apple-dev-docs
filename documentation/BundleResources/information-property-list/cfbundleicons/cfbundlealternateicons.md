# CFBundleAlternateIcons

**Framework**: Bundle Resources  
**Kind**: dictionary

A list of alternate icons for the Home screen and Settings app.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Discussion

The value of this key is different in iOS and tvOS.

In tvOS, the value of the key is an array of strings. The value of each string is the name of an icon file in your app.

In iOS, the value of the key is a dictionary. The key for each dictionary entry is the name of the alternate icon, which is also the string you pass to [`setAlternateIconName(_:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/setAlternateIconName(_:completionHandler:)) when changing icons. The value for each dictionary key is an [`AppIconReferenceName`](information-property-list/cfbundleicons/cfbundlealternateicons/appiconreferencename.md) dictionary.

## Topics

### Property List Keys
- [AppIconReferenceName](information-property-list/cfbundleicons/cfbundlealternateicons/appiconreferencename.md)

## See Also

- [CFBundlePrimaryIcon](information-property-list/cfbundleicons/cfbundleprimaryicon.md)
  The app’s primary icon for display on the Home Screen, in the Settings app, and many other places throughout the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleicons/cfbundlealternateicons)*