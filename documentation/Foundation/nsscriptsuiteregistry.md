# NSScriptSuiteRegistry

**Framework**: Foundation  
**Kind**: class

The top-level repository of scriptability information for an app at runtime.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSScriptSuiteRegistry
```

#### Overview

Scriptability information specifies the terminology available for use in scripts that target an application. It also provides information, used by AppleScript and by Cocoa, about how support for that terminology is implemented in the application. This information includes descriptions of the scriptable object classes in an application and of the commands the application supports.

There are two standard formats for supplying scriptability information: the older script suite format, consisting of a script suite file and one or more script terminology files, and the newer scripting definition (or sdef) format, consisting of a single sdef file.

There is one instance of `NSScriptSuiteRegistry` per scriptable application. This registry object collects scriptability information when the application first needs to respond to an Apple event for which Cocoa hasn’t installed a default event handler. It then creates one instance of  [`NSScriptClassDescription`](nsscriptclassdescription.md) for each object class and one instance of [`NSScriptCommandDescription`](nsscriptcommanddescription.md) for each command class, and installs a command handler for each command.

When a user executes an AppleScript script, Apple events are sent to the targeted application. Using the information stored in the registry object, Cocoa automatically converts incoming Apple events into script commands (based on [`NSScriptCommand`](nsscriptcommand.md) or a subclass) that manipulate objects in the application.

The public methods of `NSScriptSuiteRegistry` are used primarily by Cocoa’s built-in scripting support. You should not need to create a subclass of `NSScriptSuiteRegistry`.

For information on scriptability information formats, loading of scriptability information, and related topics, see “Scriptability Information” in [`Overview of Cocoa Support for Scriptable Applications`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_about_apps/SAppsAboutApps.html#//apple_ref/doc/uid/TP40001976) in [`Cocoa Scripting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Topics

### Getting and Setting the Shared Instance
- [class func setShared(NSScriptSuiteRegistry)](nsscriptsuiteregistry/setshared(_:).md)
  Sets the single, shared instance of `NSScriptSuiteRegistry` to `registry`.
- [class func shared() -> NSScriptSuiteRegistry](nsscriptsuiteregistry/shared.md)
  Returns the single, shared instance of `NSScriptSuiteRegistry`, creating it first if it doesn’t exist.
### Getting Suite Information
- [func suite(forAppleEventCode: FourCharCode) -> String?](nsscriptsuiteregistry/suite(forappleeventcode:).md)
  Returns the name of the suite definition associated with the given four-character Apple event code, `code`.
- [var suiteNames: [String]](nsscriptsuiteregistry/suitenames.md)
  Returns the names of the suite definitions currently loaded by the application.
### Getting and Registering Class Descriptions
- [func classDescriptions(inSuite: String) -> [String : NSScriptClassDescription]?](nsscriptsuiteregistry/classdescriptions(insuite:).md)
  Returns the class descriptions contained in the suite identified by `suiteName`.
- [func classDescription(withAppleEventCode: FourCharCode) -> NSScriptClassDescription?](nsscriptsuiteregistry/classdescription(withappleeventcode:).md)
  Returns the class description associated with the given four-character Apple event code, `code`.
- [func register(NSScriptClassDescription)](nsscriptsuiteregistry/register(_:)-9aplw.md)
  Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.
### Getting and Registering Command Descriptions
- [func commandDescriptions(inSuite: String) -> [String : NSScriptCommandDescription]?](nsscriptsuiteregistry/commanddescriptions(insuite:).md)
  Returns the command descriptions contained in the suite identified by `suiteName`.
- [func commandDescription(withAppleEventClass: FourCharCode, andAppleEventCode: FourCharCode) -> NSScriptCommandDescription?](nsscriptsuiteregistry/commanddescription(withappleeventclass:andappleeventcode:).md)
  Returns the command description identified by a suite’s four-character Apple event code of the class (`eventClass`) and the four-character Apple event code of the command (`commandCode`).
- [func register(NSScriptCommandDescription)](nsscriptsuiteregistry/register(_:)-5mq91.md)
  Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.
### Getting Other Suite Information
- [func aeteResource(String) -> Data?](nsscriptsuiteregistry/aeteresource(_:).md)
  Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.
- [func appleEventCode(forSuite: String) -> FourCharCode](nsscriptsuiteregistry/appleeventcode(forsuite:).md)
  Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.
- [func bundle(forSuite: String) -> Bundle?](nsscriptsuiteregistry/bundle(forsuite:).md)
  Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.
### Loading Suites
- [func loadSuite(with: [AnyHashable : Any], from: Bundle)](nsscriptsuiteregistry/loadsuite(with:from:).md)
  Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.
- [func loadSuites(from: Bundle)](nsscriptsuiteregistry/loadsuites(from:).md)
  Loads the suite definitions in bundle `aBundle`, invoking [`loadSuite(with:from:)`](nsscriptsuiteregistry/loadsuite(with:from:).md) for each suite found.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSScriptClassDescription](nsscriptclassdescription.md)
  A scriptable class that a macOS app supports.
- [class NSClassDescription](nsclassdescription.md)
  An abstract class that provides the interface for querying the relationships and properties of a class.
- [class NSScriptCommandDescription](nsscriptcommanddescription.md)
  A script command that a macOS app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry)*