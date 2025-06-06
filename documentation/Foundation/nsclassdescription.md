# NSClassDescription

**Framework**: Foundation  
**Kind**: class

An abstract class that provides the interface for querying the relationships and properties of a class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSClassDescription
```

#### Overview

Concrete subclasses of `NSClassDescription` provide the available attributes of objects of a particular class and the relationships between that class and other classes. Defining these relationships between classes allows for more intelligent and flexible manipulation of objects with key-value coding.

It is important to note that there are no class descriptions by default. To use `NSClassDescription` objects in your code you have to implement them for your model classes. For all concrete subclasses, you must provide implementations for all instance methods of `NSClassDescription`. (`NSClassDescription` provides only the implementation for the class methods that maintain the cache of registered class descriptions.) Once created, you must register a class description with the `NSClassDescription` method [`register(_:for:)`](nsclassdescription/register(_:for:).md).

You can use the `NSString` objects in the arrays returned by methods such as [`attributeKeys`](nsclassdescription/attributekeys.md) and [`toManyRelationshipKeys`](nsclassdescription/tomanyrelationshipkeys.md)  to access—using key-value coding—the properties of an instance of the class to which a class description object corresponds. For more about attributes and relationships, see Cocoa Fundamentals Guide. For more about key-value coding, see [`Key-Value Coding Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

[`NSScriptClassDescription`](nsscriptclassdescription.md), which is used to map the relationships between scriptable classes, is the only concrete subclass of `NSClassDescription` provided as part of the Cocoa framework.

## Topics

### Working with class descriptions
- [init?(for: AnyClass)](nsclassdescription/init(for:).md)
  Returns the class description for a given class.
- [class func invalidateClassDescriptionCache()](nsclassdescription/invalidateclassdescriptioncache.md)
  Removes all `NSClassDescription` objects from the cache.
- [class func register(NSClassDescription, for: AnyClass)](nsclassdescription/register(_:for:).md)
  Registers an `NSClassDescription` object for a given class in the `NSClassDescription` cache.
### Attribute keys
- [var attributeKeys: [String]](nsclassdescription/attributekeys.md)
  Overridden by subclasses to return the names of attributes of instances of the described class.
### Relationship keys
- [func inverse(forRelationshipKey: String) -> String?](nsclassdescription/inverse(forrelationshipkey:).md)
  Overridden by subclasses to return the name of the inverse relationship from a relationship specified by a given key.
- [var toManyRelationshipKeys: [String]](nsclassdescription/tomanyrelationshipkeys.md)
  Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.
- [var toOneRelationshipKeys: [String]](nsclassdescription/toonerelationshipkeys.md)
  Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.
### Notifications
- [static let NSClassDescriptionNeededForClass: NSNotification.Name](nsnotification/name-swift.struct/nsclassdescriptionneededforclass.md)
  Posted by [`init(for:)`](nsclassdescription/init(for:).md) when a class description cannot be found for a class.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSScriptClassDescription](nsscriptclassdescription.md)
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
- [class NSScriptClassDescription](nsscriptclassdescription.md)
  A scriptable class that a macOS app supports.
- [class NSScriptCommandDescription](nsscriptcommanddescription.md)
  A script command that a macOS app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription)*