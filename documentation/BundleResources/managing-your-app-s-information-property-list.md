# Managing Your App’s Information Property List

**Framework**: Bundle Resources

Create and customize an information property list file for your app using Xcode.

#### Overview

All bundles, which represent executables, must contain an information property list file describing the bundle. The details of what to include in the property list vary by executable type and by platform. It’s typically best to rely on Xcode to help create the information property list file for a given bundle.

##### Create a New Project

Xcode supplies an information property list file when you create a project from a template, as described in [`Create a project`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev07db0e578). By default, Xcode names this file `Info.plist` and adds it to your project as a source file that you can edit.

![Screenshot of Xcode showing the information property list file in a project.](https://docs-assets.developer.apple.com/published/5fd3df1bd87f5372483f3275a3b5f689/media-3376275%402x.png)

Xcode creates one information property list for each target in the project folder. For example, watchOS apps that depend on an iOS app require a separate information property list for each of the watchOS and iOS targets.

Xcode sets some property list keys automatically when creating the file. For example, Xcode sets the [`UIMainStoryboardFile`](information-property-list/uimainstoryboardfile.md) key to specify the main storyboard file in an iOS app that uses storyboards. Xcode sets certain other keys with variable values to be replaced at build time using build settings, like [`CFBundleIdentifier`](information-property-list/cfbundleidentifier.md) with a value of `$(PRODUCT_BUNDLE_IDENTIFIER)`.

##### Configure the Target

You can change some of the default settings and add others by configuring your project or target in Xcode. For example, changing the bundle identifier field in the target’s General pane affects the value of the `PRODUCT_BUNDLE_IDENTIFIER` build setting.

![Screenshot of Xcode highlighting the Bundle Identifier field in the General pane of an iOS app project.](https://docs-assets.developer.apple.com/published/0a6c43151151ee55f20b9441ff68f67d/media-3376276%402x.png)

As noted in the previous section, this build setting controls the value of the [`CFBundleIdentifier`](information-property-list/cfbundleidentifier.md) key. For more information about configuring the target, go to [`Prepare for app distribution`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev91fe7130a) and [`Add a capability to a target`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev88ff319e7).

##### Edit the Information Property List

If necessary, you can edit the information property list directly in Xcode using the property list editor. You can add or remove keys, or change their values directly. For more information, see [`Edit property lists`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev3f399a2a6).

##### Localize the Information Property List

Many strings in the information property list are human-readable strings displayed to the user, so you should localize the file. For example, localize [`CFBundleDisplayName`](information-property-list/cfbundledisplayname.md), [`CFBundleName`](information-property-list/cfbundlename.md), and all of the `UsageDescription` keys found in [`Protected resources`](protected-resources.md). For more information, go to [`Make a resource localizable`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev7c584bb2a).

##### Add Platform and Device Specific Keys

You can add platform- or device-specific keys to the information property list file by using this syntax for the key:

`[key name]-[platform]~[device]`

In this syntax, `platform` and `device` are optional qualifiers that restrict the value for the key to the platform or device. For example, use the `UISupportedInterfaceOrientations~ipad` key to set different orientation values for iPad devices.

The possible values for `platform` are:

- `iphoneos`
- `macos`

The possible values for `device` are:

- `iphone`
- `ipod`
- `ipad`

##### Build the Apps Information Property List

When you build your app, Xcode copies the source property list file from your project into the compiled bundle before code signing the bundle. It ensures that the final file has the correct name and resides in the correct location for the given bundle type.

During the copy operation, Xcode uses build settings to perform variable substitution. It also inserts additional keys representing configuration that you specify in other ways. For example, you indicate the deployment target for an iOS app in Xcode’s project editor. Xcode translates that into the [`MinimumOSVersion`](information-property-list/minimumosversion.md) key that it adds during the copy. As a result of these changes, the information property list file that ships with your app isn’t identical to the source file in your project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/managing-your-app-s-information-property-list)*