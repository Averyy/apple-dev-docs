# CIFilterGenerator

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

An object that creates and configures chains of individual image filters.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CIFilterGenerator
```

```objc
@interface CIFilterGenerator : NSObject
```

#### Overview

The `CIFilterGenerator` class provides methods for creating a [`CIFilter`](./cifilter-swift.class.md) object by chaining together existing `CIFilter` objects to create complex effects. (A **filter chain** refers to the `CIFilter` objects that are connected in the `CIFilterGenerator` object.) The complex effect can be encapsulated as a [`CIFilterGenerator`](./cifiltergenerator.md) object and saved as a file so that it can be used again. The **filter generator file** contains an archived instance  of all the `CIFilter` objects that are chained together.

Any filter generator files that you copy to `/Library/Graphics/Image Units/` are loaded when any of the loading methods provided by the [`CIPlugIn`](./ciplugin.md) class are invoked. A `CIFilterGenerator` object is registered by its filename or, if present, by a class attribute that you supply in its description.

You can create a  `CIFilterGenerator` object  programmatically, using the methods provided by the `CIFilterGenerator` class, or by using the editor view provided by Core Image.

## Topics

### Initializing a Filter Generator Object
- [init?(contentsOf: URL)](./cifiltergenerator/init%28contentsof%29.md)
  Initializes a filter generator object with the contents of a filter generator file.
### Connecting and Disconnecting Objects
- [func connect(Any, withKey: String?, to: Any, withKey: String)](./cifiltergenerator/connect%28_,withkey,to,withkey%29.md)
  Adds an object to the filter chain.
- [func disconnectObject(Any, withKey: String, to: Any, withKey: String)](./cifiltergenerator/disconnectobject%28_,withkey,to,withkey%29.md)
  Removes the connection between two objects in the filter chain.
### Managing Exported Keys
- [var exportedKeys: [AnyHashable : Any]](./cifiltergenerator/exportedkeys.md)
  Returns an array of the exported keys.
- [func exportKey(String, from: Any, withName: String?)](./cifiltergenerator/exportkey%28_,from,withname%29.md)
  Exports an input or output key of an object in the filter chain.
- [func removeExportedKey(String)](./cifiltergenerator/removeexportedkey%28_%29.md)
  Removes a key that was previously exported.
- [func setAttributes([AnyHashable : Any], forExportedKey: String)](./cifiltergenerator/setattributes%28_,forexportedkey%29.md)
  Sets a dictionary of attributes for an exported key.
### Setting and Getting Class Attributes
- [var classAttributes: [AnyHashable : Any]](./cifiltergenerator/classattributes.md)
  The class attributes associated with the filter.
### Archiving a Filter Generator Object
- [func write(to: URL, atomically: Bool) -> Bool](./cifiltergenerator/write%28to,atomically%29.md)
  Archives a filter generator object to a filter generator file.
### Registering a Filter Chain
- [func registerFilterName(String)](./cifiltergenerator/registerfiltername%28_%29.md)
  Registers the name associated with a filter chain.
### Creating a Filter from a Filter Chain
- [func filter() -> CIFilter](./cifiltergenerator/filter%28%29.md)
  Creates a filter object based on the filter chain.
### Constants
- [Exported Keys](./exported-keys.md)
  Keys for the exported parameters of a filter generator object.
### Initializers
- [init?(coder: NSCoder)](./cifiltergenerator/init%28coder%29.md)
- [init?(contentsOfURL: URL)](./cifiltergenerator/init%28contentsofurl%29-4nqjf.md)
- [init?(contentsOfURL: URL)](./cifiltergenerator/init%28contentsofurl%29-8q8ic.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CIFilterConstructor](./cifilterconstructor.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Image Units
- [class CIPlugIn](./ciplugin.md)
  The mechanism for loading image units in macOS.
- [protocol CIPlugInRegistration](./cipluginregistration.md)
  The interface for loading Core Image image units.
- [protocol CIFilterConstructor](./cifilterconstructor.md)
  A general interface for objects that produce filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator)*