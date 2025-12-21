# App execution

**Framework**: Bundle Resources

Control app launch, execution, and termination.

#### Overview

Your app interacts with the system during normal execution by calling system APIs. However, you need to communicate information about how to execute your app before you have access to these API calls. For example, you may need to specify under what conditions your app can launch, the environment that it should launch into, and what should happen when it terminates. You add keys to your app’s [`Information Property List`](information-property-list.md) file to manage its execution.

## Topics

### Launch
- [NSPrincipalClass](information-property-list/nsprincipalclass.md)
  The name of the bundle’s main executable class.
- [CLKComplicationPrincipalClass](information-property-list/clkcomplicationprincipalclass.md)
  The name of the class that implements the complication data source protocol.
- [CFBundleExecutable](information-property-list/cfbundleexecutable.md)
  The name of the bundle’s executable file.
- [LSEnvironment](information-property-list/lsenvironment.md)
  Environment variables to set before launching the app.
- [UIApplicationShortcutItems](information-property-list/uiapplicationshortcutitems.md)
### Launch conditions
- [UIRequiredDeviceCapabilities](information-property-list/uirequireddevicecapabilities.md)
  The device-related features that your app requires to run.
- [LSMultipleInstancesProhibited](information-property-list/lsmultipleinstancesprohibited.md)
  A Boolean value indicating whether more than one user can launch the app simultaneously.
- [LSArchitecturePriority](information-property-list/lsarchitecturepriority.md)
  An array of the architectures that the app supports, arranged according to their preferred usage.
- [LSRequiresNativeExecution](information-property-list/lsrequiresnativeexecution.md)
  A Boolean value that indicates whether to require the execution of the app’s native architecture when multiple architectures are available.
- [WKPrefersNetworkUponForeground](information-property-list/wkprefersnetworkuponforeground.md)
  A Boolean value that indicates whether an app requires network access on launch.
- [WKRunsIndependentlyOfCompanionApp](information-property-list/wkrunsindependentlyofcompanionapp.md)
  A Boolean value indicating whether the user can install and run the watchOS app independently of its iOS companion app.
- [WKWatchOnly](information-property-list/wkwatchonly.md)
  A Boolean value indicating whether the app is a watch-only app.
- [PUICAutoLaunchAudioOptOut](information-property-list/puicautolaunchaudiooptout.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [CLKComplicationSupportedFamilies](information-property-list/clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.
### Extensions and services
- [NSExtension](information-property-list/nsextension.md)
  The properties of an app extension.
- [NSServices](information-property-list/nsservices.md)
  The services provided by an app.
- [WKExtensionDelegateClassName](information-property-list/wkextensiondelegateclassname.md)
  The name of your watchOS app’s extension delegate.
- [UIApplicationShortcutWidget](information-property-list/uiapplicationshortcutwidget.md)
  The bundle ID of the widget that’s available as a Home screen quick action in apps that have more than one widget.
### App clips
- [NSAppClip](information-property-list/nsappclip.md)
  A collection of keys that an App Clip uses to get additional capabilities.
### Background execution
- [UIBackgroundModes](information-property-list/uibackgroundmodes.md)
  Services provided by an app that require it to run in the background.
- [WKBackgroundModes](information-property-list/wkbackgroundmodes.md)
  The services a watchOS app provides that require it to continue running in the background.
- [BGTaskSchedulerPermittedIdentifiers](information-property-list/bgtaskschedulerpermittedidentifiers.md)
  An array of strings containing developer-specified task identifiers in reverse URL notation.
- [LSBackgroundOnly](information-property-list/lsbackgroundonly.md)
  A Boolean value indicating whether the app runs only in the background.
### Endpoint security
- [NSEndpointSecurityEarlyBoot](information-property-list/nsendpointsecurityearlyboot.md)
- [NSEndpointSecurityRebootRequired](information-property-list/nsendpointsecurityrebootrequired.md)
### Plug-in support
- [NSDockTilePlugIn](information-property-list/nsdocktileplugin.md)
  The name of the app’s plug-in bundle.
### Plug-in configuration
- [CFPlugInDynamicRegisterFunction](information-property-list/cfplugindynamicregisterfunction.md)
  The function to use when dynamically registering a plug-in.
- [CFPlugInDynamicRegistration](information-property-list/cfplugindynamicregistration.md)
  A Boolean value indicating whether the host loads this plug-in.
- [CFPlugInFactories](information-property-list/cfpluginfactories.md)
  The interfaces supported by the plug-in for static registration.
- [CFPlugInTypes](information-property-list/cfplugintypes.md)
  One or more groups of interfaces supported by the plug-in for static registration.
- [CFPlugInUnloadFunction](information-property-list/cfpluginunloadfunction.md)
  The name of the function to call to unload the plug-in code from memory.
### Termination
- [LSGetAppDiedEvents](information-property-list/lsgetappdiedevents.md)
  A Boolean value indicating whether the app is notified when a child process dies.
- [NSSupportsSuddenTermination](information-property-list/nssupportssuddentermination.md)
  A Boolean value indicating whether the system may terminate the app to log out or shut down more quickly.
- [UIApplicationExitsOnSuspend](information-property-list/uiapplicationexitsonsuspend.md)
  A Boolean value indicating whether the app terminates, rather than moves to the background, when the app quits.
### Logging
- [OSLogPreferences](information-property-list/oslogpreferences.md)
  A dictionary that defines the logging configuration profile for the app.

## See Also

- [Bundle configuration](bundle-configuration.md)
  Define basic characteristics of a bundle, like its name, type, and version.
- [User interface](user-interface.md)
  Configure an app’s scenes, storyboards, icons, fonts, and other user interface elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/app-execution)*