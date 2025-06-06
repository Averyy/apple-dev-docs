# NSNib

**Framework**: AppKit  
**Kind**: class

An object wrapper, or container, for an Interface Builder nib file.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSNib
```

#### Overview

An [`NSNib`](nsnib.md) object keeps the contents of a nib file resident in memory, ready for unarchiving and instantiation. When you create a nib object using the contents of a nib file, the object loads the contents of the referenced nib bundle—the object graph as well as any images and sounds—into memory; but it does not yet unarchive it. To unarchive all of the nib data and thus truly instantiate the nib you must call one of the `instantiate...` methods of `NSNib`.

During the instantiation process, each object in the archive is unarchived and then initialized using the method befitting its type. View classes are initialized using their [`init(frame:)`](nsview/init(frame:).md) method. Custom objects are initialized using their `init` method. In the case of Cocoa views (and custom views that have options on an associated Interface Builder palette) the initialization process also reads in any values set by the user in Interface Builder.

Once all objects have been instantiated and initialized from the archive, the nib loading code attempts to reestablish the connections between each object’s outlets and the corresponding target objects. If your custom objects have outlets, the `NSNib` object attempts to reestablish any connections you created in Interface Builder. It starts by trying to establish the connections using your object’s own methods first. For each outlet that needs a connection, the [`NSNib`](nsnib.md) object looks for a method of the form `set:` in your object. If that method exists, the nib object calls it, passing the target object as a parameter. If you did not define a setter method with that exact name, the [`NSNib`](nsnib.md) object searches the object for an instance variable (of type `IBOutlet id`) with the corresponding outlet name and tries to set its value directly. If an instance variable with the correct name cannot be found, initialization of that connection does not occur.

After all objects have been initialized and their connections reestablished, each object receives an [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()) message. You can override this method in your custom objects to perform any additional initialization.

##### Subclassing Notes

You can subclass `NSNib` if you want to extend or specialize nib-loading behavior. For example, you could create a custom `NSNib` subclass that performs some post-processing on the top-level objects returned from the `instantiateNib...` methods. If you want to modify how nib instantiations are performed, it is recommended that you override the primitive method [`instantiate(withOwner:topLevelObjects:)`](nsnib/instantiate(withowner:toplevelobjects:).md). Note that the instance variables of `NSNib` are private and thus are not available to subclasses. Any override of [`init(nibData:bundle:)`](nsnib/init(nibdata:bundle:).md) or [`init(nibNamed:bundle:)`](nsnib/init(nibnamed:bundle:).md) should first invoke the superclass implementation.

## Topics

### Initializing a Nib
- [init?(nibNamed: NSNib.Name, bundle: Bundle?)](nsnib/init(nibnamed:bundle:).md)
  Returns an `NSNib` object initialized to the nib file in the specified bundle.
- [init(nibData: Data, bundle: Bundle?)](nsnib/init(nibdata:bundle:).md)
  Initializes an instance with nib data and specified bundle for locating resources.
- [typealias Name](nsnib/name.md)
### Instantiating a Nib
- [func instantiate(withOwner: Any?, topLevelObjects: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](nsnib/instantiate(withowner:toplevelobjects:).md)
  Instantiates objects in the nib file with the specified owner.
### Constants
- [Nib Loading Keys](nib-loading-keys.md)
  The `NSNib` class uses the following constants which are used as keys in the dictionary passed to [`instantiateNibWithExternalNameTable:`](nsnib/instantiatenibwithexternalnametable:.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnib)*