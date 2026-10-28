# HMAccessoryCategory

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

A category for a HomeKit accessory.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMAccessoryCategory
```

```objc
@interface HMAccessoryCategory : NSObject
```

## Overview

A category represents a class of devices, like light bulbs or outlets. You can use a category to help users identify the types of accessories they’re browsing. For example, when adding a lamp and a fan to a home, users might not be able to distinguish these accessories if you display only the manufacturer name and model number for each accessory. To improve the user experience, you can use the category information associated with each accessory to help the user understand which accessory is the lamp and which is the fan.

## Topics

### Reading the category type
- [var categoryType: String](./hmaccessorycategory/categorytype.md)
  The category to which this accessory belongs.
- [Accessory Category Types](./accessory-category-types.md)
  The accessory category types supported by HomeKit.
### Describing the category
- [var localizedDescription: String](./hmaccessorycategory/localizeddescription.md)
  A localized description of the category.

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

### Categorizing an accessory
- [var category: HMAccessoryCategory](./hmaccessory/category.md)
  The category to which the accessory belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorycategory)*