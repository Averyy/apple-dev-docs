# phoneticRepresentation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The phonetic representation name components of the receiver.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var phoneticRepresentation: PersonNameComponents? { get set }
```

```objc
@property (copy, nullable) NSPersonNameComponents * phoneticRepresentation;
```

## Discussion

Each component of the receiver with a value should have a corresponding value for any value set for this property. `nil` by default.

The `phoneticRepresentation` property value of this property value is ignored.

## See Also

### Accessing Person Name Components
- [var namePrefix: String?](./nameprefix.md)
  The portion of a name’s full form of address that precedes the name itself *(for example, “Dr.,” “Mr.,” “Ms.”)*.
- [var givenName: String?](./givenname.md)
  Name bestowed upon an individual to differentiate them from other members of a group that share a family name *(for example, “Johnathan”)*.
- [var middleName: String?](./middlename.md)
  Secondary name bestowed upon an individual to differentiate them from others that have the same given name *(for example, “Maple”)*.
- [var familyName: String?](./familyname.md)
  Name bestowed upon an individual to denote membership in a group or family. *(for example, “Appleseed”)*.
- [var nameSuffix: String?](./namesuffix.md)
  The portion of a name’s full form of address that follows the name itself *(for example, “Esq.,” “Jr.,” “Ph.D.”)*.
- [var nickname: String?](./nickname.md)
  Name substituted for the purposes of familiarity *(for example, “Johnny”)*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/phoneticrepresentation)*