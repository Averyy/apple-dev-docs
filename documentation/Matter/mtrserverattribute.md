# MTRServerAttribute

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRServerAttribute
```

## Topics

### Initializers
- [init?(readonlyAttributeWithID: NSNumber, initialValue: [String : Any], requiredPrivilege: MTRAccessControlEntryPrivilege)](mtrserverattribute/init(readonlyattributewithid:initialvalue:requiredprivilege:).md)
### Instance Properties
- [var attributeID: NSNumber](mtrserverattribute/attributeid.md)
- [var isWritable: Bool](mtrserverattribute/iswritable.md)
- [var requiredReadPrivilege: MTRAccessControlEntryPrivilege](mtrserverattribute/requiredreadprivilege.md)
- [var value: [String : Any]](mtrserverattribute/value.md)
### Instance Methods
- [func setValue([String : Any]) -> Bool](mtrserverattribute/setvalue(_:).md)
### Type Methods
- [class func newFeatureMapAttribute(withInitialValue: NSNumber) -> Self](mtrserverattribute/newfeaturemapattribute(withinitialvalue:).md)
  Create an attribute description for a FeatureMap attribute with the provided value (expected to be an unsigned integer representing the value of the bitmap). This will automatically set requiredPrivilege to the right value for FeatureMap.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrserverattribute)*