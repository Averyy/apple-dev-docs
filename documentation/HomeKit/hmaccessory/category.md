# category

**Framework**: HomeKit  
**Kind**: property

The category to which the accessory belongs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var category: HMAccessoryCategory { get }
```

#### Discussion

The accessory’s [`category`](hmaccessory/category.md) property contains an instance of the [`HMAccessoryCategory`](hmaccessorycategory.md) class that indicates the kind of accessory, like light bulb, garage door opener, or faucet. Use this information to help users distinguish among different accessories in their environment.

## See Also

- [class HMAccessoryCategory](hmaccessorycategory.md)
  A category for a HomeKit accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/category)*