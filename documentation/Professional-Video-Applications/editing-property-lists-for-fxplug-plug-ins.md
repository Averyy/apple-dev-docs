# Editing property lists for FxPlug plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Modify the way hosts recognize and display your FxPlug plug-in.

## Overview

FxPlug plug-ins typically have more than one `Info.plist` file: one in the application bundle and one in the XPC service. Although the application’s `Info.plist` doesn’t require any changes, your XPC’s `Info.plist` requires some changes to create a functioning plug-in.

Add the following key-value pairs to your XPC `Info.plist,` using the associated values listed below for your plug-in. Below is an example of a complete `Info.plist`.

![A screen shot showing the complete Info.plist key-value pairs.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3915368@2x.png)

> 💡 **Tip**:  Add entries to property lists by control-clicking in the blank space below the last entry and selecting Add Row, or hovering the mouse over an existing entry and clicking the + button. After selecting the appropriate key (or typing it in manually) change the type for the type of key you require (String, Number, Dictionary, Array, etc.) To add components to a Dictionary or Array, first turn down the arrow before clicking the + button.

### Add PlugInKit dictionary

This dictionary contains three items: A `PrincipalClass` key, a `Protocol` key, and an `Attributes` dictionary with the component keys `com.apple.protocol` with the string value `FxPlug`, and `com.apple.version` with a version number. Set the `Protocol` key to `PROXPCProtocol`, as this is what is used to identify your plug-in as an FxPlug to PlugInKit. Set the `PrincipalClass` string here to [`FxPrincipal`](../professional_video_applications/fxprincipal.md).

By adding these keys, you make your XPC discoverable by PlugInKit. It’s important to update your version number when you make updates—if the host app finds more than one plug-in with the same name, it returns the plug-in with the newest version first.

### Add ProPlugPlugInGroupList and ProPlugPlugInList keys

Both of these keys are arrays of values that tell the host application how to name and categorize your effect.

Here’s a short description of what each one does:

`ProPlugPlugInGroupList` lists the `groupName` and the group’s UUID to which your plug-in should be added. You can provide a new `groupName` and group UUID, or use an existing one. If multiple plug-ins list the same group UUID, they’re joined together in that group when displayed in Motion’s Library.

In the `ProPlugPlugInList` dictionary, enter your plug-in’s `className`, `displayName`, `infoString`, `version`, and two different UUIDs, one for the plug-in, and one that matches the group’s UUID defined in `ProPlugPlugInGroupList`. To avoid conflicts when the host loads plug-ins, every effect needs its own unique UUID, so generate a new one if you duplicate an example project. Note that the `protocolNames` entry still requires either `FxFilter` or `FxGenerator`, even though those classes are deprecated, so that host apps know what kind of effect your plug-in is.

> 💡 **Tip**:  Generate new UUIDs from the command line with the `uuidgen` command, which you can then copy and paste into your plist.

### Add XPCService entry

There are some new keys to be added to this entry:

`RunLoopType` with a String value of “`_NSApplication`”,

`JoinExistingSession` with a Boolean value of `YES`, and

`_AdditionalSubServices`, a dictionary that contains a key “viewbridge”, and a Boolean value of `YES`.

> **Note**:  There are underscores within some of these key-value pairs, so add them with caution.

### Add ProPlugDynamicRegistration and ProPlugDynamicRegistrationPrincipalClass keys

Your plug-in bundle may have a static list of plug-ins a host app should register, or it may leave registration to the bundle’s principal class. With a static list, plug-ins are recognized and loaded automatically; for a dynamic list, the bundle’s principal class is asked to register the plug-ins. The distinction depends on the value of the Boolean tag `ProPlugDynamicRegistration` in the property list. In the example below, the property list has listed `YES` for this key, so the plug-in bundle will use dynamic registration.

If you use dynamic registration, you need to add additional key/values in your XPC’s `Info.plist` PluginKit section. Add the key `ProPlugDynamicRegistrationPrincipalClass` and make the value the name of the registrar class. Also add a key for `ProPlugDictionaryVersion` to the XPC’s `Info.plist`.

![The Info.plist from the FxDynamicRegistration example plug-in showing ProPlugDynamicRegistration and ProPlugDynamicRegistrationPrincipalClass keys.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3559529@2x.png)

Dynamic registration incurs a plug-in scanning performance hit. Use static registration whenever possible. You can find more information about dynamic registration in `PROPlugInRegistering` or `<PluginManager/PROPlugInBundleRegistration.h>`.

## See Also

### Plug-in fundamentals
- [Building an FxPlug plug-in from an Xcode template](./building-an-fxplug-plug-in-from-an-xcode-template.md)
  Create a plug-in in Xcode with the FxPlug template.
- [Building an FxPlug plug-in manually](./building-an-fxplug-plug-in-manually.md)
  Create your own plug-in in Xcode.
- [Using FxPlug APIs](./using-fxplug-apis.md)
  Use various FxPlug APIs to communicate with host apps like Motion or Final Cut Pro.
- [Thread safety in plug-ins](./thread-safety-in-plug-ins.md)
  Learn about reentrancy for plug-ins and best practices to make them thread safe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/editing-property-lists-for-fxplug-plug-ins)*