# Notarizing your FxPlug plug-in

**Framework**: Professional-Video-Applications  
**Role**: Article

Give users confidence in your FxPlug plug-in by enabling notarization.

#### Overview

[Code signing](https://developer.apple.com/support/code-signing/) your plug-in assures users that it’s from a known source and that modifications haven’t occurred since its certification. You must sign your plug-in with a certificate from Apple before you can integrate app services, install it on a device, or submit it to the App Store.

You can give users even more confidence in the Apple-certified software that you distribute by [Notarizing macOS software before distribution](../Security/notarizing-macos-software-before-distribution.md). Notarization is not the same as app review. The Apple notary service is an automated system that scans your software for malicious content, checks for code-signing issues, and returns the results to you quickly. If there are no issues, the notary service generates a ticket for you to staple to your software. The notary service also publishes that ticket online where [Gatekeeper](https://developer.apple.com/developer-id/) can find it.

When the user first installs or runs your plug-in, the presence of a ticket (either online or as an attachment to the executable) tells Gatekeeper that Apple notarized the software. Gatekeeper then places descriptive information in the initial launch dialog so the user can make an informed choice about whether to launch the plug-in’s wrapper application.

##### Set up for code signing your plug-in

If you haven’t already, enroll in the [Apple Developer Program](https://developer.apple.com/programs/), then follow the [Signing & Capabilities workflow](https://help.apple.com/xcode/mac/current/#/dev60b6fbbc7) instructions and generate a Developer ID certificate for macOS distribution. Apple recommends [automatic signing](https://help.apple.com/xcode/mac/current/#/dev80cc24546).

##### Set your plug-in’s code signing team and signing certificate

The FxPlug template and FxPlug Example projects are set to Sign to Run Locally, but you need to change this to your own signing certificate for your targets to enable code signing.

For Wrapper Application and XPC Service targets, select your Team (if applicable) and the signing certificate you prepared in the previous step.

##### Set your XPC service’s code signing inject base entitlements

You must set your XPC Service target’s Code Signing Inject Base Entitlements to `YES` to ensure your plug-in loads correctly in Final Cut Pro and Motion. Select your XPC Service target, then select the Build Settings tab, and find Code Signing Inject Base Entitlements in the Signing section.

##### Code sign embedded frameworks

You must copy the `FxPlug.framework` to the XPC Service target of FxPlug plug-ins and turn on Code Sign On Copy to automatically code sign the framework when it copies to the bundle. Add other frameworks as necessary.

> ❗ **Important**:  Occasionally, frameworks like `PluginManager.framework` may not be compatible with the Code Sign On Copy feature in Xcode, and you must force code sign them with a script. To force code sign a framework, use the following command in your script: `codesign --force --timestamp --options runtime --sign “${CODE_SIGN_IDENTITY}” “${BUILT_PRODUCTS_DIR}/${FRAMEWORKS_FOLDER_PATH}/FrameworkName.framework”.`

![A screenshot showing the script for copying and force code signing the PluginManager.framework.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-4193577@2x.png)

> ❗ **Important**:  Deselect the “Based on dependency analysis” checkbox in the “Run script” options, and set “User Script Sandboxing” to No in Build Settings.

##### Enable Hardened Runtime

[Hardened runtime](https://help.apple.com/xcode/mac/current/#/devf87a2ac8f) provides security protection for your plug-ins and is a requirement for notarizing a macOS plug-in. You must enable the hardened runtime capability and declare entitlements for the functions your plug-in requires.

1. Select the Xcode Project, then select the Wrapper Application target and click Signing & Capabilities.
2. If Hardened Runtime isn’t already visible, click Capability and then double-click Hardened Runtime.
3. Select any Runtime Exceptions or Resource Access options your plug-in requires.

![A screenshot showing the Hardened runtime option for the Wrapper Application.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-4193576@2x.png)

You can check for errors by building and running your plug-in, and then launching Console and searching for the process name of your plug-in.

##### Generate a notarized distributable version

Before distributing your plug-in directly to customers, you must sign it with your Developer ID. Xcode’s Organizer window includes a workflow for generating a distributable version of your app. In Xcode 10 and later, this workflow includes an option to notarize your FxPlug plug-in automatically. Notarize your app using the following workflow:

1. Open your Xcode project.
2. Create an archive of your app.
3. Open Xcode’s Organizer window.
4. In the Archives tab, select the archive you created.
5. Click Distribute App to view the distribution options.
6. Select Developer ID for your method of distribution, and then click Next.
7. Select Upload to send your archive to the Apple notary service, and then click Next.

![A screenshot showing the upload option for sending your archive to the Apple Notary Service.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3915698@2x.png)

Xcode uploads your archive to the notary service. When the upload is complete, the notary service begins the scanning process, which usually takes less than an hour. While the notary service scans your software, you can continue preparing your archive for distribution. For example, you can export the archive and perform any final testing prior to making your software available to customers.

When the notarization process finishes, Xcode downloads the ticket and staples it to your archive. Export your archive again to receive a distributable version of your plug-in that includes the notary ticket.

See [Notarizing macOS software before distribution](../Security/notarizing-macos-software-before-distribution.md), [Upload a macOS app to be notarized](https://help.apple.com/xcode/mac/current/#/dev88332a81e), and [Resolving common notarization issues](../Security/resolving-common-notarization-issues.md) for more information about this process.

## See Also

### Testing and deployment
- [Testing FxPlug plug-ins](./testing-fxplug-plug-ins.md)
  Test and debug FxPlug plug-ins using a variety of methods.
- [Preparing plug-ins for use in Final Cut Pro](./preparing-plug-ins-for-use-in-final-cut-pro.md)
  Add a plug-in to a Motion effect template to use in Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/notarizing-your-fxplug-plug-in)*