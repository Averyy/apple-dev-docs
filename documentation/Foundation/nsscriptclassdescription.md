# NSScriptClassDescription

**Framework**: Foundation  
**Kind**: class

A scriptable class that a macOS app supports.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSScriptClassDescription
```

#### Overview

A scriptable application provides scriptability information that describes the commands and objects scripters can use in scripts that target the application. That includes information about the classes those scriptable objects are created from.

An application’s scriptability information is collected automatically by an instance of [`NSScriptSuiteRegistry`](nsscriptsuiteregistry.md). The registry object creates an `NSScriptClassDescription` for each class it finds and caches these objects in memory. Cocoa scripting uses registry information in handling scripting requests that target the application.

A class description instance stores the name, attributes, relationships, and supported commands for a class. For example, a scriptable `document` class for a drawing application might support attributes such as `file` and `file type`, relationships such as collections of `circles`, `rectangles`, and `lines`, and commands such as `align` and `rotate`.

As with many of the classes in Cocoa’s built-in scripting support, your application may never need to directly work with instances of `NSScriptClassDescription`. However, one case where you might need access to a class description is if you override `objectSpecifier` in a scriptable class. For information on how to do this, see [`Object Specifiers`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_object_specifiers/SAppsObjectSpecifiers.html#//apple_ref/doc/uid/TP40002164-CH3) in [`Cocoa Scripting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

Another case where your application may need access to class description information is if you override `indicesOfObjectsByEvaluatingWithContainer:count:` in a specifier class.

Although you can subclass `NSScriptClassDescription`, it is unlikely that you would need to do so, or even to create instances of it.

## Topics

### Initializing a Script Class Description
- [init?(suiteName: String, className: String, dictionary: [AnyHashable : Any]?)](nsscriptclassdescription/init(suitename:classname:dictionary:).md)
  Initializes and returns a newly allocated instance of `NSScriptClassDescription`.
### Getting a Script Class Description
- [init?(for: AnyClass)](nsscriptclassdescription/init(for:).md)
  Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.
- [func forKey(String) -> NSScriptClassDescription?](nsscriptclassdescription/forkey(_:).md)
  Returns the class description instance for the class type of the specified attribute or relationship.
- [var superclass: NSScriptClassDescription?](nsscriptclassdescription/superclass.md)
  Returns the class description instance for the superclass of the receiver’s class.
### Getting basic information about the script class
- [var className: String?](nsscriptclassdescription/classname.md)
  Returns the name of the class the receiver describes, as provided at initialization time.
- [var defaultSubcontainerAttributeKey: String?](nsscriptclassdescription/defaultsubcontainerattributekey.md)
  Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [var implementationClassName: String?](nsscriptclassdescription/implementationclassname.md)
  Returns the name of the Objective-C class instantiated to implement the scripting class.
- [func isLocationRequiredToCreate(forKey: String) -> Bool](nsscriptclassdescription/islocationrequiredtocreate(forkey:).md)
  Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.
- [var suiteName: String?](nsscriptclassdescription/suitename.md)
  Returns the name of the receiver’s suite.
### Getting and comparing Apple event codes
- [var appleEventCode: FourCharCode](nsscriptclassdescription/appleeventcode.md)
  Returns the Apple event code associated with the receiver’s class.
- [func appleEventCode(forKey: String) -> FourCharCode](nsscriptclassdescription/appleeventcode(forkey:).md)
  Returns the Apple event code for the specified attribute or relationship in the receiver.
- [func matchesAppleEventCode(FourCharCode) -> Bool](nsscriptclassdescription/matchesappleeventcode(_:).md)
  Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.
### Getting attribute and relationship information
- [func hasOrderedToManyRelationship(forKey: String) -> Bool](nsscriptclassdescription/hasorderedtomanyrelationship(forkey:).md)
  Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [func hasProperty(forKey: String) -> Bool](nsscriptclassdescription/hasproperty(forkey:).md)
  Returns a Boolean value indicating whether the described class has a property identified by the specified key.
- [func hasReadableProperty(forKey: String) -> Bool](nsscriptclassdescription/hasreadableproperty(forkey:).md)
  Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.
- [func hasWritableProperty(forKey: String) -> Bool](nsscriptclassdescription/haswritableproperty(forkey:).md)
  Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [func key(withAppleEventCode: FourCharCode) -> String?](nsscriptclassdescription/key(withappleeventcode:).md)
  Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.
- [func type(forKey: String) -> String?](nsscriptclassdescription/type(forkey:).md)
  Returns the name of the declared type of the attribute or relationship identified by the passed key.
### Getting command information
- [func selector(forCommand: NSScriptCommandDescription) -> Selector?](nsscriptclassdescription/selector(forcommand:).md)
  Returns the selector associated with the receiver for the specified command description.
- [func supportsCommand(NSScriptCommandDescription) -> Bool](nsscriptclassdescription/supportscommand(_:).md)
  Returns a Boolean value indicating whether the receiver or any superclass supports the specified command.

## Relationships

### Inherits From
- [NSClassDescription](nsclassdescription.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSScriptSuiteRegistry](nsscriptsuiteregistry.md)
  The top-level repository of scriptability information for an app at runtime.
- [class NSClassDescription](nsclassdescription.md)
  An abstract class that provides the interface for querying the relationships and properties of a class.
- [class NSScriptCommandDescription](nsscriptcommanddescription.md)
  A script command that a macOS app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription)*