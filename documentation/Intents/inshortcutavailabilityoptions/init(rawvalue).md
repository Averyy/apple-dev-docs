# init(rawValue:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Returns the set of availability categories represented by the given value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(rawValue: UInt)
```

## Discussion

It’s unlikely that your code should call this directly. Instead, refer to the static members to create an [`OptionSet`](../../Swift/optionset.md) of [`INShortcutAvailabilityOptions`](../inshortcutavailabilityoptions.md).

## Parameters

- `rawValue`: An unsigned integer expressing the union of the options for the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcutavailabilityoptions/init(rawvalue:))*