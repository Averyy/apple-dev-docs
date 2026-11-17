# AgeRangeService.AgeRangeDeclaration.confirmed

**Framework**: Declared Age Range  
**Kind**: case  
**Role**: Case

A status that indicates a person confirmed their age-range declaration.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+
- macOS 26.5+

## Declaration

```swift
case confirmed
```

## Discussion

A person can confirm their age-range declaration in one of the following ways:

- Taking a selfie
- Providing a credit card
- Scanning a government ID

For more information about selfie-based age confirmation, see [Confirm that you’re an adult with a selfie](https://support.apple.com/en-us/149095). For the other methods, see [How to confirm that you’re an adult](https://support.apple.com/en-us/125662).

## See Also

### Determining the age set method
- [AgeRangeService.AgeRangeDeclaration.selfDeclared](./selfdeclared.md)
  Indicates the person signed in to iCloud to set their own age range.
- [AgeRangeService.AgeRangeDeclaration.guardianDeclared](./guardiandeclared.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/confirmed)*