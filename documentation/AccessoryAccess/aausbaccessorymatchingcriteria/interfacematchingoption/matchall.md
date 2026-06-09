# AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption.matchAll

**Framework**: Accessory Access  
**Kind**: case

A value that indicates the match needs to be all inclusive of the provided interface criteria.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
case matchAll
```

#### Discussion

Matching is successful for the USB accessory that has at least one USB interface matching every criteria in the provided dictionary.

## See Also

- [init?(rawValue: Int)](aausbaccessorymatchingcriteria/interfacematchingoption/init(rawvalue:).md)
  Initializes a new interface matching option with the provided value.
- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption.matchAny](aausbaccessorymatchingcriteria/interfacematchingoption/matchany.md)
  A value that indicates that the match needs to cover at least one of the provided interface criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/interfacematchingoption/matchall)*