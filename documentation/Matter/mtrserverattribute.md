# MTRServerAttribute

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRServerAttribute : NSObject
```

## Topics

### Initializers
- [init?(readonlyAttributeWithID: NSNumber, initialValue: [String : Any], requiredPrivilege: MTRAccessControlEntryPrivilege)](./mtrserverattribute/init%28readonlyattributewithid,initialvalue,requiredprivilege%29.md)
### Instance Properties
- [var attributeID: NSNumber](./mtrserverattribute/attributeid.md)
- [var isWritable: Bool](./mtrserverattribute/iswritable.md)
- [var requiredReadPrivilege: MTRAccessControlEntryPrivilege](./mtrserverattribute/requiredreadprivilege.md)
- [var value: [String : Any]](./mtrserverattribute/value.md)
### Instance Methods
- [func setValue([String : Any]) -> Bool](./mtrserverattribute/setvalue%28_%29.md)
### Type Methods
- [class func newFeatureMapAttribute(withInitialValue: NSNumber) -> Self](./mtrserverattribute/newfeaturemapattribute%28withinitialvalue%29.md)
  Create an attribute description for a FeatureMap attribute with the provided value (expected to be an unsigned integer representing the value of the bitmap). This will automatically set requiredPrivilege to the right value for FeatureMap.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrserverattribute)*