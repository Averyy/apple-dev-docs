# CFBundle

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFBundle
```

#### Overview

CFBundle allows you to use a folder hierarchy called a bundle to organize and locate many types of application resources including images, sounds, localized strings, and executable code. In macOS, bundles can also be used by CFM applications to load and execute functions from Mach-O frameworks. You can use bundles to support multiple languages or execute your application on multiple operating environments.

You create a bundle object using one of the `CFBundleCreate...` functions. CFBundle provides several functions for finding resources within a bundle. The [`CFBundleCopyResourceURL(_:_:_:_:)`](cfbundlecopyresourceurl(_:_:_:_:).md) function returns the location of a resource of the specified name and type, and in the specified subdirectory. Use [`CFBundleCopyResourceURLForLocalization(_:_:_:_:_:)`](cfbundlecopyresourceurlforlocalization(_:_:_:_:_:).md) to restrict the search to a specific localization name. Use [`CFBundleCopyResourceURLsOfType(_:_:_:)`](cfbundlecopyresourceurlsoftype(_:_:_:).md) to get the locations of all resources of a specified type.

CFBundle provides functions for getting bundle information, such as its identifier and information dictionary. Use the [`CFBundleGetIdentifier(_:)`](cfbundlegetidentifier(_:).md) function to get the identifier of a bundle, and the [`CFBundleGetInfoDictionary(_:)`](cfbundlegetinfodictionary(_:).md) function to get its information dictionary. The principal intended purpose for locating bundles by identifier is so that code (in frameworks, plugins, etc.) can find its own bundle.

You can also obtain locations of subdirectories in a bundle represented as CFURL objects. The [`CFBundleCopyExecutableURL(_:)`](cfbundlecopyexecutableurl(_:).md) function returns the location of the application’s executable. The functions [`CFBundleCopyResourceURL(_:_:_:_:)`](cfbundlecopyresourceurl(_:_:_:_:).md), [`CFBundleCopySharedFrameworksURL(_:)`](cfbundlecopysharedframeworksurl(_:).md), [`CFBundleCopyPrivateFrameworksURL(_:)`](cfbundlecopyprivateframeworksurl(_:).md), [`CFBundleCopySharedSupportURL(_:)`](cfbundlecopysharedsupporturl(_:).md), and [`CFBundleCopyBuiltInPlugInsURL(_:)`](cfbundlecopybuiltinpluginsurl(_:).md) return the location of a bundle’s subdirectory containing resources, shared frameworks, private frameworks, shared support files, and plug-ins respectively.

Other functions are used to manage localizations. The [`CFBundleCopyLocalizedString(_:_:_:_:)`](cfbundlecopylocalizedstring(_:_:_:_:).md) and [`CFBundleCopyLocalizationsForURL(_:)`](cfbundlecopylocalizationsforurl(_:).md) functions return a localized string from a bundle’s strings file. The [`CFBundleCopyLocalizationsForPreferences(_:_:)`](cfbundlecopylocalizationsforpreferences(_:_:).md) function returns the localizations that CFBundle would prefer, given the specified bundle and user preference localizations.

Unlike some other Core Foundation opaque types with similar Cocoa Foundation names (such as CFString and `NSString`), [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) objects cannot be cast (“toll-free bridged”) to CFBundle objects.

Unlike `NSBundle`, which does not support unloading (because the Objective C runtime does not support the unloading of Objective C code), you can unload CFBundle objects.

[`CFBundleGetFunctionPointerForName(_:_:)`](cfbundlegetfunctionpointerforname(_:_:).md) and related calls automatically load a bundle if it is not already loaded. When the last reference to the CFBundle object is released and it is finally deallocated, then the code will be unloaded if it is still loaded and if the executable is of a type that supports unloading. If you keep this in mind, and if you make sure that everything that uses the bundle keeps a retain on the CFBundle object, then you can just use the bundle naturally and never have to worry about when it is loaded and unloaded.

On the other hand, if you want to manually manage when the bundle is loaded and unloaded, then you can use [`CFBundleLoadExecutable(_:)`](cfbundleloadexecutable(_:).md) and [`CFBundleUnloadExecutable(_:)`](cfbundleunloadexecutable(_:).md)—although this technique is not recommended. These functions force immediate loading and unloading of the executable (if it has not already been loaded/unloaded, and in the case of unloading if the executable is of a type that supports unloading). If you do this, then the code calling `CFBundleUnloadExecutable` is responsible for making sure that there are no remaining references to anything in the bundle’s code before it is unloaded. In the previous approach, by contrast, this responsibility can be distributed to the individual code sections that use the bundle, by making sure that each one keeps its own retain on the CFBundle object.

One further point about CFBundle reference counting: if you are taking the first approach, but do not actually wish the bundle’s code to be unloaded (as is often the case), or if you are taking the second approach of manually managing the unloading yourself, then in many cases you do not actually have to worry about releasing a CFBundle object. CFBundle instances are uniqued, so there is only one CFBundle object for a given bundle, and rarely are there so many bundles being considered at once that the memory usage for CFBundle objects would be significant. There are cases in which a process could create CFBundle objects for potentially an unlimited number of bundles, and such processes would wish to balance retains and releases carefully, but such cases are likely to be rare.

Note that it is best to compile any unloadable bundles with the flag `-fno-constant-cfstrings`—see [`Bundle Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i) for more details.

## Topics

### Creating and Accessing Bundles
- [func CFBundleCreate(CFAllocator!, CFURL!) -> CFBundle!](cfbundlecreate(_:_:).md)
  Creates a CFBundle object.
- [func CFBundleCreateBundlesFromDirectory(CFAllocator!, CFURL!, CFString!) -> CFArray!](cfbundlecreatebundlesfromdirectory(_:_:_:).md)
  Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [func CFBundleGetAllBundles() -> CFArray!](cfbundlegetallbundles().md)
  Returns an array containing all of the bundles currently open in the application.
- [func CFBundleGetBundleWithIdentifier(CFString!) -> CFBundle!](cfbundlegetbundlewithidentifier(_:).md)
  Locate a bundle given its program-defined identifier.
- [func CFBundleGetMainBundle() -> CFBundle!](cfbundlegetmainbundle().md)
  Returns an application’s main bundle.
### Loading and Unloading a Bundle
- [func CFBundleIsExecutableLoaded(CFBundle!) -> Bool](cfbundleisexecutableloaded(_:).md)
  Obtains information about the load status for a bundle’s main executable.
- [func CFBundlePreflightExecutable(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfbundlepreflightexecutable(_:_:).md)
  Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [func CFBundleLoadExecutable(CFBundle!) -> Bool](cfbundleloadexecutable(_:).md)
  Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [func CFBundleLoadExecutableAndReturnError(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfbundleloadexecutableandreturnerror(_:_:).md)
  Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
- [func CFBundleUnloadExecutable(CFBundle!)](cfbundleunloadexecutable(_:).md)
  Unloads the main executable for the specified bundle.
### Finding Locations in a Bundle
- [func CFBundleCopyAuxiliaryExecutableURL(CFBundle!, CFString!) -> CFURL!](cfbundlecopyauxiliaryexecutableurl(_:_:).md)
  Returns the location of a bundle’s auxiliary executable code.
- [func CFBundleCopyBuiltInPlugInsURL(CFBundle!) -> CFURL!](cfbundlecopybuiltinpluginsurl(_:).md)
  Returns the location of a bundle’s built in plug-in.
- [func CFBundleCopyExecutableURL(CFBundle!) -> CFURL!](cfbundlecopyexecutableurl(_:).md)
  Returns the location of a bundle’s main executable code.
- [func CFBundleCopyPrivateFrameworksURL(CFBundle!) -> CFURL!](cfbundlecopyprivateframeworksurl(_:).md)
  Returns the location of a bundle’s private Frameworks directory.
- [func CFBundleCopyResourcesDirectoryURL(CFBundle!) -> CFURL!](cfbundlecopyresourcesdirectoryurl(_:).md)
  Returns the location of a bundle’s Resources directory.
- [func CFBundleCopySharedFrameworksURL(CFBundle!) -> CFURL!](cfbundlecopysharedframeworksurl(_:).md)
  Returns the location of a bundle’s shared frameworks directory.
- [func CFBundleCopySharedSupportURL(CFBundle!) -> CFURL!](cfbundlecopysharedsupporturl(_:).md)
  Returns the location of a bundle’s shared support files directory.
- [func CFBundleCopySupportFilesDirectoryURL(CFBundle!) -> CFURL!](cfbundlecopysupportfilesdirectoryurl(_:).md)
  Returns the location of the bundle’s support files directory.
### Locating Bundle Resources
- [func CFBundleCloseBundleResourceMap(CFBundle!, CFBundleRefNum)](cfbundleclosebundleresourcemap(_:_:).md)
  Closes an open resource map for a bundle.
- [func CFBundleCopyResourceURL(CFBundle!, CFString!, CFString!, CFString!) -> CFURL!](cfbundlecopyresourceurl(_:_:_:_:).md)
  Returns the location of a resource contained in the specified bundle.
- [func CFBundleCopyResourceURLInDirectory(CFURL!, CFString!, CFString!, CFString!) -> CFURL!](cfbundlecopyresourceurlindirectory(_:_:_:_:).md)
  Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [func CFBundleCopyResourceURLsOfType(CFBundle!, CFString!, CFString!) -> CFArray!](cfbundlecopyresourceurlsoftype(_:_:_:).md)
  Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [func CFBundleCopyResourceURLsOfTypeInDirectory(CFURL!, CFString!, CFString!) -> CFArray!](cfbundlecopyresourceurlsoftypeindirectory(_:_:_:).md)
  Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.
- [func CFBundleCopyResourceURLForLocalization(CFBundle!, CFString!, CFString!, CFString!, CFString!) -> CFURL!](cfbundlecopyresourceurlforlocalization(_:_:_:_:_:).md)
  Returns the location of a localized resource in a bundle.
- [func CFBundleCopyResourceURLsOfTypeForLocalization(CFBundle!, CFString!, CFString!, CFString!) -> CFArray!](cfbundlecopyresourceurlsoftypeforlocalization(_:_:_:_:).md)
  Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [func CFBundleOpenBundleResourceFiles(CFBundle!, UnsafeMutablePointer<CFBundleRefNum>!, UnsafeMutablePointer<CFBundleRefNum>!) -> Int32](cfbundleopenbundleresourcefiles(_:_:_:).md)
  Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps.
- [func CFBundleOpenBundleResourceMap(CFBundle!) -> CFBundleRefNum](cfbundleopenbundleresourcemap(_:).md)
  Opens the non-localized and localized resource files (if any) for a bundle in a single resource map.
### Managing Localizations
- [func CFBundleCopyBundleLocalizations(CFBundle!) -> CFArray!](cfbundlecopybundlelocalizations(_:).md)
  Returns an array containing a bundle’s localizations.
- [func CFBundleCopyLocalizedString(CFBundle!, CFString!, CFString!, CFString!) -> CFString!](cfbundlecopylocalizedstring(_:_:_:_:).md)
  Returns a localized string from a bundle’s strings file.
- [func CFBundleCopyLocalizationsForPreferences(CFArray!, CFArray!) -> CFArray!](cfbundlecopylocalizationsforpreferences(_:_:).md)
  Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [func CFBundleCopyLocalizationsForURL(CFURL!) -> CFArray!](cfbundlecopylocalizationsforurl(_:).md)
  Returns an array containing the localizations for a bundle or executable at a particular location.
- [func CFBundleCopyPreferredLocalizationsFromArray(CFArray!) -> CFArray!](cfbundlecopypreferredlocalizationsfromarray(_:).md)
  Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.
### Managing Executable Code
- [func CFBundleGetDataPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetdatapointerforname(_:_:).md)
  Returns a data pointer to a symbol of the given name.
- [func CFBundleGetDataPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetdatapointersfornames(_:_:_:).md)
  Returns a C array of data pointer to symbols of the given names.
- [func CFBundleGetFunctionPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetfunctionpointerforname(_:_:).md)
  Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [func CFBundleGetFunctionPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetfunctionpointersfornames(_:_:_:).md)
  Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [func CFBundleGetPlugIn(CFBundle!) -> CFPlugIn!](cfbundlegetplugin(_:).md)
  Returns a bundle’s plug-in.
### Getting Bundle Properties
- [func CFBundleCopyBundleURL(CFBundle!) -> CFURL!](cfbundlecopybundleurl(_:).md)
  Returns the location of a bundle.
- [func CFBundleGetDevelopmentRegion(CFBundle!) -> CFString!](cfbundlegetdevelopmentregion(_:).md)
  Returns the bundle’s development region from the bundle’s information property list.
- [func CFBundleGetIdentifier(CFBundle!) -> CFString!](cfbundlegetidentifier(_:).md)
  Returns the bundle identifier from a bundle’s information property list.
- [func CFBundleGetInfoDictionary(CFBundle!) -> CFDictionary!](cfbundlegetinfodictionary(_:).md)
  Returns a bundle’s information dictionary.
- [func CFBundleGetLocalInfoDictionary(CFBundle!) -> CFDictionary!](cfbundlegetlocalinfodictionary(_:).md)
  Returns a bundle’s localized information dictionary.
- [func CFBundleGetValueForInfoDictionaryKey(CFBundle!, CFString!) -> CFTypeRef!](cfbundlegetvalueforinfodictionarykey(_:_:).md)
  Returns a value (localized if possible) from a bundle’s information dictionary.
- [func CFBundleCopyInfoDictionaryInDirectory(CFURL!) -> CFDictionary!](cfbundlecopyinfodictionaryindirectory(_:).md)
  Returns a bundle’s information dictionary.
- [func CFBundleCopyInfoDictionaryForURL(CFURL!) -> CFDictionary!](cfbundlecopyinfodictionaryforurl(_:).md)
  Returns the information dictionary for a given URL location.
- [func CFBundleGetPackageInfo(CFBundle!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!)](cfbundlegetpackageinfo(_:_:_:).md)
  Returns a bundle’s package type and creator.
- [func CFBundleGetPackageInfoInDirectory(CFURL!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!) -> Bool](cfbundlegetpackageinfoindirectory(_:_:_:).md)
  Returns a bundle’s package type and creator without having to create a CFBundle object.
- [func CFBundleCopyExecutableArchitectures(CFBundle!) -> CFArray!](cfbundlecopyexecutablearchitectures(_:).md)
  Returns an array of CFNumbers representing the architectures a given bundle provides.
- [func CFBundleCopyExecutableArchitecturesForURL(CFURL!) -> CFArray!](cfbundlecopyexecutablearchitecturesforurl(_:).md)
  Returns an array of CFNumbers representing the architectures a given URL provides.
- [func CFBundleGetVersionNumber(CFBundle!) -> UInt32](cfbundlegetversionnumber(_:).md)
  Returns a bundle’s version number.
### Getting the CFBundle Type ID
- [func CFBundleGetTypeID() -> CFTypeID](cfbundlegettypeid().md)
  Returns the type identifier for the CFBundle opaque type.
### Data Types
- [typealias CFBundleRefNum](cfbundlerefnum.md)
  Type that identifies a distinct reference number for a resource map.
### Constants
- [Information Property List Keys](information-property-list-keys.md)
  Standard keys found in a bundle’s information property list file.
- [Architecture Types](1537096-architecture-types.md)
  Constants that identify executable architecture types.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Bundle Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundle)*