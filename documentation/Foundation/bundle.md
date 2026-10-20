# Bundle

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A representation of the code and resources stored in a bundle directory on disk.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class Bundle
```

```objc
@interface NSBundle : NSObject
```

#### Overview

Apple uses bundles to represent apps, frameworks, plug-ins, and many other specific types of content. Bundles organize their contained resources into well-defined subdirectories, and bundle structures vary depending on the platform and the type of the bundle. By using a bundle object, you can access a bundle’s resources without knowing the structure of the bundle. The bundle object provides a single interface for locating items, taking into account the bundle structure, user preferences, available localizations, and other relevant factors.

Any executable can use a bundle object to locate resources, either inside an app’s bundle or in a known bundle located elsewhere. You don’t use a bundle object to locate files in a container directory or in other parts of the file system.

The general pattern for using a bundle object is as follows:

1. Create a bundle object for the intended bundle directory.
2. Use the methods of the bundle object to locate or load the needed resource.
3. Use other system APIs to interact with the resource.

Some types of frequently used resources can be located and opened without a bundle. For example, when loading images, you store images in asset catalogs and load them using the [`init(named:)`](../UIKit/uiimage/init%28named%29.md) methods of [`UIImage`](../UIKit/uiimage.md) or [`NSImage`](../AppKit/nsimage.md). Similarly, for string resources, you use [`NSLocalizedString`](./nslocalizedstring.md) to load individual strings instead of loading the entire `.strings` file yourself.

> **Note**: Unlike some other Foundation classes with corresponding Core Foundation names (such as [`NSString`](./nsstring.md) and [`CFString`](../CoreFoundation/cfstring.md)), [`Bundle`](./bundle.md) objects cannot be cast to [`CFBundle`](../CoreFoundation/cfbundle.md) references. If you need functionality provided by [`CFBundle`](../CoreFoundation/cfbundle.md), you can still create a [`CFBundle`](../CoreFoundation/cfbundle.md) and use the [`CFBundle`](../CoreFoundation/cfbundle.md) API. See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

##### Finding and Opening a Bundle

Before you can locate a resource, you must first specify which bundle contains it. The [`Bundle`](./bundle.md) class has many constructors, but the one you use most often is [`main`](./bundle/main.md). The main bundle represents the bundle directory that contains the currently executing code. So for an app, the main bundle object gives you access to the resources that shipped with your app.

If your app interacts directly with plug-ins, frameworks, or other bundled content, you can use other methods of this class to create appropriate bundle objects. You can always create bundle objects from a known URL or path, but other methods make it easier to access bundles your app is already using. For example, if you link to a framework, you can use the [`init(for:)`](./bundle/init%28for%29.md) method to locate the framework bundle based on a class defined in that framework.

**Swift**:

```swift
// Get the app's main bundle
let mainBundle = Bundle.main

// Get the bundle containing the specified private class.
let myBundle = Bundle(for: NSClassFromString("MyPrivateClass")!)
```

**Objective-C**:

```objc
// Get the app's main bundle
NSBundle *main = [NSBundle mainBundle];

// Get the bundle containing the specified private class.
NSBundle *myBundle = [NSBundle bundleForClass:[MyPrivateClass class]];
```

In Swift, use the [`bundle()`](./bundle%28%29.md) macro to insert a bundle instance appropriate to the current execution context, whether an app, app extension, framework, or Swift package.

##### Locating Resources in a Bundle

You use [`Bundle`](./bundle.md) objects to obtain the location of specific resources inside the bundle. When looking for resources, you provide the name of the resource and its type at a minimum. For resources in a specific subdirectory, you can also specify that directory. After locating the resource, the bundle routines return a path string or URL that you can use to open the file.

Locating a single resource in a bundle

```objc
NSBundle *main = [NSBundle mainBundle];
NSString *resourcePath = [main pathForResource:@"Seagull" ofType:@"jpg"];
```

Bundle objects follow a specific search pattern when looking for resources on disk. Global resources—that is, resources not in a language-specific `.lproj` directory—are returned first, followed by region- and language-specific resources. This search pattern means that the bundle looks for resources in the following order:

1. Global (nonlocalized) resources
2. Region-specific localized resources (based on the user’s region preferences)
3. Language-specific localized resources (based on the user’s language preferences)
4. Development language resources (as specified by the [CFBundleDevelopmentRegion](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-130430) key in the bundle’s Info.plist file)

Because global resources take precedence over language-specific resources, you should never include both a global and localized version of a given resource in your app. When a global version of a resource exists, language-specific versions are never returned. The reason for this precedence is performance. If localized resources were searched first, the bundle object might waste time searching for a nonexistent localized resource before returning the global resource.

> ❗ **Important**:  Bundle objects always consider case when searching for resource files, even on file systems that support case-insensitive filenames. Always make sure that you specify filenames with case sensitivity in mind.

When locating resource files, the bundle object automatically considers many standard filename modifiers when determining which file to return. Resources may be tagged for a specific device (`~iphone`, `~ipad`) or for a specific screen resolution (`@2x`, `@3x`). Do not include these modifiers when specifying the name of the resource you want. The bundle object selects the file that is most appropriate for the underlying device. For more information, see [App Icons on iPhone, iPad and Apple Watch](https://developer.apple.com/library/archive/qa/qa1686/_index.html#//apple_ref/doc/uid/DTS40009882).

##### Understanding Bundle Structures

Bundle structures vary depending on the target platform and the type of bundle you are building. The [`Bundle`](./bundle.md) class hides this underlying structure in most (but not all) cases. Many of the methods you use to load resources from a bundle automatically locate the appropriate starting directory and look for resources in known places. You can also use the methods and properties of this class to get the location of known bundle directories and to retrieve resources specifically from those directories.

For information about the bundle structure of iOS and macOS apps, see [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i). For information about the structure of framework bundles, see [Framework Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Frameworks.html#//apple_ref/doc/uid/10000183i). For information about the structure of macOS plug-ins, see [Code Loading Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/LoadingCode.html#//apple_ref/doc/uid/10000052i).

## Topics

### Getting standard bundle objects
- [class var main: Bundle](./bundle/main.md)
  Returns the bundle object that contains the current executable.
- [class var allFrameworks: [Bundle]](./bundle/allframeworks.md)
  Returns an array of all of the application’s bundles that represent frameworks.
- [class var allBundles: [Bundle]](./bundle/allbundles.md)
  Returns an array of all the application’s non-framework bundles.
### Creating and initializing a bundle
- [convenience init?(url: URL)](./bundle/init%28url%29-a2t0.md)
  Returns an `NSBundle` object that corresponds to the specified file URL.
- [init(for: AnyClass)](./bundle/init%28for%29.md)
  Returns the `NSBundle` object with which the specified class is associated.
- [init?(identifier: String)](./bundle/init%28identifier%29.md)
  Returns the `NSBundle` instance that has the specified bundle identifier.
- [init?(path: String)](./bundle/init%28path%29.md)
  Returns an `NSBundle` object initialized to correspond to the specified directory.
### Loading nib files
- [func loadNibNamed(String, owner: Any?, options: [UINib.OptionsKey : Any]?) -> [Any]?](./bundle/loadnibnamed%28_,owner,options%29.md)
  Unarchives the contents of a nib file located in the receiver’s bundle.
- [func loadNibNamed(NSNib.Name, owner: Any?, topLevelObjects: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](./bundle/loadnibnamed%28_,owner,toplevelobjects%29.md)
  Loads a nib from the bundle with the specified file name and owner.
### Finding resource files
- [func url(forResource: String?, withExtension: String?, subdirectory: String?) -> URL?](./bundle/url%28forresource,withextension,subdirectory%29.md)
  Returns the file URL for the resource file identified by the specified name and extension and residing in a given bundle directory.
- [func url(forResource: String?, withExtension: String?) -> URL?](./bundle/url%28forresource,withextension%29.md)
  Returns the file URL for the resource identified by the specified name and file extension.
- [func urls(forResourcesWithExtension: String?, subdirectory: String?) -> [URL]?](./bundle/urls%28forresourceswithextension,subdirectory%29.md)
  Returns an array of file URLs for all resources identified by the specified file extension and located in the specified bundle subdirectory.
- [func url(forResource: String?, withExtension: String?, subdirectory: String?, localization: String?) -> URL?](./bundle/url%28forresource,withextension,subdirectory,localization%29.md)
  Returns the file URL for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.
- [func urls(forResourcesWithExtension: String?, subdirectory: String?, localization: String?) -> [URL]?](./bundle/urls%28forresourceswithextension,subdirectory,localization%29.md)
  Returns an array containing the file URLs for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [class func url(forResource: String?, withExtension: String?, subdirectory: String?, in: URL) -> URL?](./bundle/url%28forresource,withextension,subdirectory,in%29.md)
  Creates and returns a file URL for the resource with the specified name and extension in the specified bundle.
- [class func urls(forResourcesWithExtension: String?, subdirectory: String?, in: URL) -> [URL]?](./bundle/urls%28forresourceswithextension,subdirectory,in%29.md)
  Returns an array containing the file URLs for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, within the specified bundle.
- [func path(forResource: String?, ofType: String?) -> String?](./bundle/path%28forresource,oftype%29.md)
  Returns the full pathname for the resource identified by the specified name and file extension.
- [func path(forResource: String?, ofType: String?, inDirectory: String?) -> String?](./bundle/path%28forresource,oftype,indirectory%29-swift.method.md)
  Returns the full pathname for the resource identified by the specified name and file extension and located in the specified bundle subdirectory.
- [func path(forResource: String?, ofType: String?, inDirectory: String?, forLocalization: String?) -> String?](./bundle/path%28forresource,oftype,indirectory,forlocalization%29.md)
  Returns the full pathname for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.
- [func paths(forResourcesOfType: String?, inDirectory: String?) -> [String]](./bundle/paths%28forresourcesoftype,indirectory%29-swift.method.md)
  Returns an array containing the pathnames for all bundle resources having the specified filename extension and residing in the resource subdirectory.
- [func paths(forResourcesOfType: String?, inDirectory: String?, forLocalization: String?) -> [String]](./bundle/paths%28forresourcesoftype,indirectory,forlocalization%29.md)
  Returns an array containing the file for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [class func path(forResource: String?, ofType: String?, inDirectory: String) -> String?](./bundle/path%28forresource,oftype,indirectory%29-swift.type.method.md)
  Returns the full pathname for the resource file identified by the specified name and extension and residing in a given bundle directory.
- [class func paths(forResourcesOfType: String?, inDirectory: String) -> [String]](./bundle/paths%28forresourcesoftype,indirectory%29-swift.type.method.md)
  Returns an array containing the pathnames for all bundle resources having the specified extension and residing in the bundle directory at the specified path.
### Finding image resources
- [func urlForImageResource(NSImage.Name) -> URL?](./bundle/urlforimageresource%28_%29.md)
  Returns the location of the specified image resource as an NSURL.
- [func pathForImageResource(NSImage.Name) -> String?](./bundle/pathforimageresource%28_%29.md)
  Returns the location of the specified image resource file.
- [func image(forResource: NSImage.Name) -> NSImage?](./bundle/image%28forresource%29.md)
  Returns an `NSImage` instance associated with the specified name, which can be backed by multiple files representing different resolution versions of the image.
### Finding sound resources
- [func path(forSoundResource: NSSound.Name) -> String?](./bundle/path%28forsoundresource%29.md)
  Returns the location of the specified sound resource file.
### Fetching localized strings
- [func localizedString(forKey: String, value: String?, table: String?) -> String](./bundle/localizedstring%28forkey,value,table%29.md)
  Returns a localized version of the string designated by the specified key and residing in the specified table.
### Fetching context help resources
- [func contextHelp(forKey: NSHelpManager.ContextHelpKey) -> NSAttributedString?](./bundle/contexthelp%28forkey%29.md)
  Returns the context-sensitive help for the specified key from the bundle’s help file.
### Getting the standard bundle directories
- [var resourceURL: URL?](./bundle/resourceurl.md)
  The file URL of the bundle’s subdirectory containing resource files.
- [var executableURL: URL?](./bundle/executableurl.md)
  The file URL of the receiver’s executable file.
- [var privateFrameworksURL: URL?](./bundle/privateframeworksurl.md)
  The file URL of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksURL: URL?](./bundle/sharedframeworksurl.md)
  The file URL of the receiver’s subdirectory containing shared frameworks.
- [var builtInPlugInsURL: URL?](./bundle/builtinpluginsurl.md)
  The file URL of the receiver’s subdirectory containing plug-ins.
- [func url(forAuxiliaryExecutable: String) -> URL?](./bundle/url%28forauxiliaryexecutable%29.md)
  Returns the file URL of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportURL: URL?](./bundle/sharedsupporturl.md)
  The file URL of the bundle’s subdirectory containing shared support files.
- [var appStoreReceiptURL: URL?](./bundle/appstorereceipturl.md)
  The file URL for the bundle’s App Store receipt.
- [var resourcePath: String?](./bundle/resourcepath.md)
  The full pathname of the bundle’s subdirectory containing resources.
- [var executablePath: String?](./bundle/executablepath.md)
  The full pathname of the receiver’s executable file.
- [var privateFrameworksPath: String?](./bundle/privateframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksPath: String?](./bundle/sharedframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing shared frameworks.
- [var builtInPlugInsPath: String?](./bundle/builtinpluginspath.md)
  The full pathname of the receiver’s subdirectory containing plug-ins.
- [func path(forAuxiliaryExecutable: String) -> String?](./bundle/path%28forauxiliaryexecutable%29.md)
  Returns the full pathname of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportPath: String?](./bundle/sharedsupportpath.md)
  The full pathname of the bundle’s subdirectory containing shared support files.
### Getting bundle information
- [var bundleURL: URL](./bundle/bundleurl.md)
  The full URL of the receiver’s bundle directory.
- [var bundlePath: String](./bundle/bundlepath.md)
  The full pathname of the receiver’s bundle directory.
- [var bundleIdentifier: String?](./bundle/bundleidentifier.md)
  The receiver’s bundle identifier.
- [var infoDictionary: [String : Any]?](./bundle/infodictionary.md)
  A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.
- [func object(forInfoDictionaryKey: String) -> Any?](./bundle/object%28forinfodictionarykey%29.md)
  Returns the value associated with the specified key in the receiver’s information property list.
### Getting localization information
- [var localizations: [String]](./bundle/localizations.md)
  A list of all the localizations contained in the bundle.
- [var preferredLocalizations: [String]](./bundle/preferredlocalizations.md)
  An ordered list of preferred localizations contained in the bundle.
- [var developmentLocalization: String?](./bundle/developmentlocalization.md)
  The localization for the development language.
- [var localizedInfoDictionary: [String : Any]?](./bundle/localizedinfodictionary.md)
  A dictionary with the keys from the bundle’s localized property list.
- [class func preferredLocalizations(from: [String]) -> [String]](./bundle/preferredlocalizations%28from%29.md)
  Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.
- [class func preferredLocalizations(from: [String], forPreferences: [String]?) -> [String]](./bundle/preferredlocalizations%28from,forpreferences%29.md)
  Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.
### Managing preservation priority for on-demand resources
- [func setPreservationPriority(Double, forTags: Set<String>)](./bundle/setpreservationpriority%28_,fortags%29.md)
  A hint to the system of the relative order for purging tagged sets of resources in the bundle.
- [func preservationPriority(forTag: String) -> Double](./bundle/preservationpriority%28fortag%29.md)
  Returns the current preservation priority for the specified tag.
### Getting classes from a bundle
- [func classNamed(String) -> AnyClass?](./bundle/classnamed%28_%29.md)
  Returns the `Class` object for the specified name.
- [var principalClass: AnyClass?](./bundle/principalclass.md)
  The bundle’s principal class.
- [class let didLoadNotification: NSNotification.Name](./bundle/didloadnotification.md)
  A notification that lets observers know when classes are dynamically loaded.
- [let NSLoadedClasses: String](./nsloadedclasses.md)
  A constant used as a key for the `userInfo` dictionary of a [`didLoadNotification`](./bundle/didloadnotification.md) notification that corresponds to an array of names of each class that was loaded.
- [Bundle.DidLoadMessage](./bundle/didloadmessage.md)
  A message a bundle sends when it dynamically loads a class.
### Loading code from a bundle
- [var executableArchitectures: [NSNumber]?](./bundle/executablearchitectures.md)
  An array of numbers indicating the architecture types supported by the bundle’s executable.
- [func preflight() throws](./bundle/preflight%28%29.md)
  Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [func load() -> Bool](./bundle/load%28%29.md)
  Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [func loadAndReturnError() throws](./bundle/loadandreturnerror%28%29.md)
  Loads the bundle’s executable code and returns any errors.
- [func unload() -> Bool](./bundle/unload%28%29.md)
  Unloads the code associated with the receiver.
- [var isLoaded: Bool](./bundle/isloaded.md)
  The load status of a bundle.
- [Mach-O Architecture](./api-1495005-mach-o-architecture.md)
  Constants that describe the CPU types that a bundle’s executable code supports.
### Errors
- [var NSExecutableErrorMinimum: Int](./nsexecutableerrorminimum-swift.var.md)
  The beginning of the range of error codes reserved for errors related to executable files.
- [var NSExecutableNotLoadableError: Int](./nsexecutablenotloadableerror-swift.var.md)
  The executable type isn’t loadable in the current process.
- [var NSExecutableArchitectureMismatchError: Int](./nsexecutablearchitecturemismatcherror-swift.var.md)
  The executable doesn’t provide an architecture compatible with the current process.
- [var NSExecutableRuntimeMismatchError: Int](./nsexecutableruntimemismatcherror-swift.var.md)
  The executable has Objective-C runtime information that’s incompatible with the current process.
- [var NSExecutableLoadError: Int](./nsexecutableloaderror-swift.var.md)
  Executable cannot be loaded for an otherwise-unspecified reason.
- [var NSExecutableLinkError: Int](./nsexecutablelinkerror-swift.var.md)
  The executable failed due to linking issues.
- [var NSExecutableErrorMaximum: Int](./nsexecutableerrormaximum-swift.var.md)
  The end of the range of error codes reserved for errors related to executable files.
### Initializers
- [convenience init?(URL: URL)](./bundle/init%28url%29-16uva.md)
- [convenience init?(URL: URL)](./bundle/init%28url%29-1y93d.md)
- [init(forClass: AnyClass)](./bundle/init%28forclass%29.md)
- [convenience init?(url: URL)](./bundle/init%28url%29-3n9rf.md)
  Returns an `NSBundle` object initialized to correspond to the specified file URL.
### Instance Methods
- [func loadAppleScriptObjectiveCScripts()](./bundle/loadapplescriptobjectivecscripts%28%29.md)
- [func localizedString(forKey: String, value: String?, table: String?, localizations: [Locale.Language]) -> String](./bundle/localizedstring%28forkey,value,table,localizations%29.md)
  Look up a localized string given a list of available languages.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Bundle Resources
- [macro bundle() -> Bundle](./bundle%28%29.md)
  Expands to a bundle instance that’s most likely to contain resources for the calling code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle)*