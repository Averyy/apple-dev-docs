# Versioning and obsoleting old plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Version plug-ins to add new capabilities, or obsolete them to remove them from the Motion Library.

#### Overview

Developers commonly add new functionalities or rendering abilities to plug-ins over time. Versioning a plug-in allows for older instances of a plug-in that are already applied to a project to maintain the old rendering behavior and new instances to use a new rendering behavior. Obsoleting a plug-in prevents the plug-in from appearing in the Motion Library, and therefore prevents new instances from being applied. However, old instances of the plug-in continue to function as long as Motion and Final Cut Pro support it.

##### Versioning a plug-in

To version a plug-in, add a version key to your plug-in’s `Info.plist`, and set a version number as a string or number.

```other
<key>version</key>
<string>1</string>
```

If a plug-in has a version number, when it is applied to an object in a project, the version number at the time it is applied is saved. That instance of the plug-in retains that version number, even if the version number of the plug-in’s `Info.plist` is later updated. This strategy works well for users because it ensures backward compatibility of renders that are created with earlier versions of your plug-in.

##### Reading a plug-in’s version number

The [`FxVersioningAPI`](../professional_video_applications/fxversioningapi.md) provides [`versionAtCreation()`](../professional_video_applications/fxversioningapi/versionatcreation%28%29.md) for reading the version number of a plug-in instance.

For example, if you release version 1 of your plug-in and a few months later you change the way it outputs pixel values, you can increase the version number to 2. You can then add the new render path to your plug-in and use it only if [`versionAtCreation()`](../professional_video_applications/fxversioningapi/versionatcreation%28%29.md) returns `2`.

##### Updating the version of a plug-in instance

Sometimes a plug-in may require an update to the version of the current plug-in instance applied in a Motion project. This version update might be most convenient to make when the user changes a parameter and therefore purges the previous render. For example, your plug-in can update the plug-in instance’s version number in the [`parameterChanged(_:at:)`](../professional_video_applications/fxtileableeffect/parameterchanged%28_,at%29.md) method by using [`FxVersioningAPI`](../professional_video_applications/fxversioningapi.md)’s [`updateVersion(atCreation:)`](../professional_video_applications/fxversioningapi/updateversion%28atcreation%29.md) to set a new version number.

##### Obsoleting a plug-in

When you release a newer plug-in, you may not want your older plug-in to appear in the host’s list of available plug-ins and instead choose to replace it with a new version with a different UUID. You could make this choice, for example, because you’ve updated from FxPlug 3 to FxPlug 4, your new plug-in requires a new license from your customers, or you’ve combined the functionality of several plug-ins into a single plug-in. In all these cases, simply versioning may not be a suitable option for your plug-in, but you still want instances of older versions to continue to function as long as the host supports them.

The solution is to use the obsolete key. When you add it to your plug-in’s `Info.plist` file with a value of `YES`, the obsolete key tells the host application not to display its name in the list of available plug-ins.

```other
<key>obsolete</key>
<string>YES</string>
```

When a user opens an existing project, the plug-in’s user interface is still available, and they can copy and paste instances of the plug-in but can’t create a new instance of the plug-in from scratch. So you can use the same name for the new plug-in and ensure that only new instances are created going forward.

Likewise, when Final Cut Pro loads a project that contains a Motion Template with an obsolete plug-in, the obsolete plug-in will work properly. Usually, developers ship only the new template with the new plug-in, and only users who installed the old plug-in with the old template can use the old version. As a result, however, the new template must have a different name from the old one or be put into a different category. Developers often avoid this issue by adding a version number to the template name, such as “My Cool Plugin v1.moef.” You can also deprecate a Motion Template. See [Deprecate a Motion template](./preparing-plug-ins-for-use-in-final-cut-pro.md#Deprecate-a-Motion-template).

## See Also

### Legacy plug-ins
- [Migrating FxPlug 3 plug-ins to FxPlug 4](./migrating-fxplug-3-plug-ins-to-fxplug-4.md)
  Update existing FxPlug 3 plug-ins to out-of-process FxPlug 4 plug-ins.
- [protocol FxVersioningAPI](../professional_video_applications/fxversioningapi.md)
  A collection of methods that a host application implements to identify the plug-in version used by a project when it was first created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/versioning-and-obsoleting-old-plug-ins)*