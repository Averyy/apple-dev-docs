# containerURL(forSecurityApplicationGroupIdentifier:)

**Framework**: Foundation  
**Kind**: method

Returns the container directory associated with the specified security application group identifier.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func containerURL(forSecurityApplicationGroupIdentifier groupIdentifier: String) -> URL?
```

#### Return Value

A URL indicating the location of the group’s shared directory in the file system. In iOS, the value is `nil` when the group identifier is invalid. In macOS, a URL of the expected form is always returned, even if the app group is invalid, so be sure to test that you can access the underlying directory before attempting to use it.

#### Discussion

Sandboxed apps in macOS and all apps in iOS that need to share files with other apps from the same developer on a given device use the [`App Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.application-groups) to join one or more application groups. The entitlement consists of an array of group identifier strings that indicate the groups to which the app belongs, as described in [`Adding an App to an App Group`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW19) in [`Entitlement Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AboutEntitlements.html#//apple_ref/doc/uid/TP40011195).

You use one of these group identifier strings to locate the corresponding group’s shared directory. When you call [`containerURL(forSecurityApplicationGroupIdentifier:)`](filemanager/containerurl(forsecurityapplicationgroupidentifier:).md) with one of your app’s group identifiers, the method returns an [`NSURL`](nsurl.md) instance specifying the location in the file system of that group’s shared directory. The behavior of application groups differs between macOS and iOS.

##### App Groups in Macos

For a sandboxed app in macOS, the group directory is located at `~/Library/Group Containers/<application-group-id>`, where the application group identifier begins with the developer’s team identifier followed by a dot, followed by the specific group name. The system creates this directory automatically the first time your app needs it and never removes it.

> **Note**:  Always use the URL returned by this method to locate the group directory rather than manually constructing a URL with an explicit path. The exact location of the directory in the file system might change in future releases of macOS, but this method will always return the correct URL.

The system also creates the `Library/Application Support`, `Library/Caches`, and `Library/Preferences` subdirectories inside the group directory the first time you use it. You are free to add or remove subdirectories as you see fit, but you are encouraged to use these standardized locations as you would in the app’s usual container.

If you call the method with an invalid group identifier, namely one for which you do not have an entitlement, the method still returns a URL of the expected form, but the corresponding group directory does not actually exist, nor can your sandboxed app create it. Therefore be sure to test that you can successfully access the returned URL before using it.

##### App Groups in Ios

In iOS, the group identifier starts with the word `group` and a dot, followed by the group name. However, the system makes no guarantee about the group directory’s name or location in the file system. Indeed, the directory is accessible only with the file URL returned by this method. As in macOS, the system creates the directory when you need it. Unlike in macOS, when all the apps in a given app group are removed from the device, the system detects this condition and removes the corresponding group directory as well.

The system creates only the `Library/Caches` subdirectory automatically, but you can create others yourself if you need them. You are free to use the group directory as you see fit, but take care to coordinate its structure among all the group’s apps.

If you call the method with an invalid group identifier in iOS, the method returns a `nil` value.

## Parameters

- `groupIdentifier`: A string that names the group whose shared directory you want to obtain. This input should exactly match one of the strings in the app’s  .

## See Also

- [App Sandbox Design Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)
- [Entitlement Key Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AboutEntitlements.html#//apple_ref/doc/uid/TP40011195)
- [App Groups Entitlement](../BundleResources/Entitlements/com.apple.security.application-groups.md)
  A list of identifiers specifying the groups your app belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/containerurl(forsecurityapplicationgroupidentifier:))*