# NSUpdateSecurityPolicy

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

#### Discussion

The `NSUpdateSecurityPolicy` property list key describes a security policy dictionary that defines the processes and packages that the system allows to modify an app’s bundle. You specify these by Team ID (any package signed by that team), or Team IDs and signing identifiers (to identify a specific executable) signed by a team.

For signed apps, macOS allows apps from the same developer — those sharing the same Team ID — to modify the app’s bundle. Use this security policy to change the default behavior and customize which specific apps or installers can write to your app’s bundle.

If this protection mechanism isn’t relevant to your app, you can opt out of this capability and disable the hardened runtime by adding the `com.apple.security.cs.disable-executable-page-protection` entitlement to your app’s `info.plist` file. For information about this entitlement — and important information about the security ramifications of disabling this protection — see [`Disable Executable Memory Protection Entitlement`](entitlements/com.apple.security.cs.disable-executable-page-protection.md).

The `NSUpdateSecurityPolicy` key is a dictionary you add to your app’s `info.plist` file in the source editor pane of your app’s Xcode target. Add the key following the instructions below, and add one or both of the dictionary’s subkeys, depending on the types of apps or installers you want to allow to perform updates to your app’s resources. The subkeys are:

- `AllowPackages`: An array of Team IDs. The operating system allows any installer package signed by any Team ID in this list to write content into this app’s bundle.
- `AllowProcesses`: A dictionary that maps Team IDs to an array of signing (bundle) IDs. The operating system allows an app (process) with the matching bundle ID that’s signed by the specified Team ID to write content into this app’s bundle.

##### Add the Policy Dictionary to Your Apps Information Property List

To add the `NSUpdateSecurityPolicy` key to your app’s `info.plist` file, follow these steps:

1. In Xcode, select your app’s target from the Target navigator, and then select the source editor pane in the detail section.
2. Control-click the last item in the list, and choose Add Row from the drop-down menu.
3. Edit the text for the new row, replacing the existing text with , and press Return.
4. Control-click  the Type field for the new row and choose Dictionary from the drop-down menu.
5. Click the disclosure triangle next to the new NSUpdateSecurityPolicy dictionary to open it (the arrow needs to point down). This ensures that in the next steps, the editor adds elements inside the dictionary, and not as separate items parallel to it in the property list.

The newly created, empty `NSUpdateSecurityPolicy` dictionary in your app’s property list resembles the image below:

![A screenshot that shows the Xcode property list editor with the addition of a new, empty dictionary supporting the NSUpdateSecurityPolicy key.](https://docs-assets.developer.apple.com/published/dec3a1965721f643417e1531c6d73e9e/media-4098859%402x.png)

Next, add one or both subcomponents to the security policy dictionary depending on your app’s update policy requirements. To allow any installer package signed by a specific Team ID, add an `AllowPackages` array to the `NSUpdateSecurityPolicy` dictionary. Using this key, the operating system allows any installer package signed by the specified Team IDs in this array to write content into the app’s bundle.

1. Control-click the NSUpdateSecurityPolicy row in the property list and choose Add Row.
2. Edit the row name, replacing the default text with  and press Return.
3. Control-click the new AllowPackages row’s Type drop-down menu and choose Array.
4. Control-click the new AllowPackages row and choose Add Row. This adds a new element to the `AllowPackages` array.
5. Set the value of the new array element to the Team ID of the team whose installers you’re authorizing to update this app.
6. Repeat steps 4 and 5 for each additional team whose installers you want to authorize.

To allow specific apps from specific teams to write to this app’s bundle, add an `AllowProcesses` dictionary to the `NSUpdateSecurityPolicy` dictionary. Using this key, and it’s subdictionaries, the operating system allows specific apps defined by both a Team ID and signing ID (also called a ) to write content into this app’s bundle.

1. Control-click the NSUpdateSecurityPolicy row in the property list and choose Add Row.
2. Edit the row name, replacing the default text with  and press Return.
3. Control-click the new AllowProcesses row’s Type drop-down menu and choose Dictionary.
4. Control-click the new AllowProcesses row and choose Add Row. This adds a new element to the AllowProcesses dictionary.
5. Control-click the new row’s Type drop-down menu, and choose Dictionary. Set the new row’s name to be the Team ID of the app or apps you want to allow to update this app’s bundle.
6. Control-click the new Team ID row, and add a row to the newly created team dictionary.
7. Control-click the new row’s Type drop-down menu and choose Array.
8. Control-click the array row, and add a new row to the array.
9. Set the value of the new array element to the signing ID (bundle ID) of the app you’re authorizing to write to the app’s bundle.
10. To add additional authorized apps for this Team ID, repeat steps 8 and 9.
11. To add additional teams and apps, repeat steps 5 through 9.

The final new `NSUpdateSecurityPolicy` dictionary resembles the configuration in the image below:

![A screenshot that shows the Xcode property list editor with the addition of the NSUpdateSecurityPolicy key and its allowsPackages and allowedProcesses components with sample values.](https://docs-assets.developer.apple.com/published/38d422bddfe218d398a9360a7e663b49/media-4098858%402x.png)

The following sample code describes a complete update policy, in JSON format, that allows any installer package signed by Team ID `Z9P22VQP42` to write to the app bundle. The policy also allows a single app associated with the bundle ID `com.example.myapp.updater` (also signed with the Team ID `Z9P22VQP42`) that can modify the app bundle.

```javascript
{
  "NSUpdateSecurityPolicy": {
    "AllowPackages": [
      0: "Z9P22VQP42"
    ]
    "AllowProcesses": {
      "Z9P22VQP42": [
        0: "com.example.myapp.updater"
      ]
    }
  }
}
```

## Topics

### Security policies
- [AllowPackages](information-property-list/nsupdatesecuritypolicy/allowpackages.md)
  An array of Team IDs that the system uses to determine whether an installer package, signed by one of the specified Team IDs, can update an app’s bundle.
- [AllowProcesses](information-property-list/nsupdatesecuritypolicy/allowprocesses.md)
  A dictionary that maps Team IDs to an array of signing (bundle) IDs that the system uses to determine whether a process can update an app’s bundle.

## See Also

- [NSAppDataUsageDescription](information-property-list/nsappdatausagedescription.md)
  A message that tells people why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingUsageDescription](information-property-list/nsusertrackingusagedescription.md)
  A message that informs the user why an app is requesting permission to use data for tracking the user or the device.
- [NSAppleEventsUsageDescription](information-property-list/nsappleeventsusagedescription.md)
  A message that tells people why the app is requesting the ability to send Apple events.
- [NSSystemAdministrationUsageDescription](information-property-list/nssystemadministrationusagedescription.md)
  A message in macOS that tells people why the app is requesting to manipulate the system configuration.
- [ITSAppUsesNonExemptEncryption](information-property-list/itsappusesnonexemptencryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](information-property-list/itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsupdatesecuritypolicy)*