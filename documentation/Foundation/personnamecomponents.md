# PersonNameComponents

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

The separate parts of a person’s name, allowing locale-aware formatting.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct PersonNameComponents
```

## Topics

### Creating Person Name Components
- [init()](./personnamecomponents/init%28%29.md)
  Initializes a new person name components structure.
### Accessing Person Name Components
- [var namePrefix: String?](./personnamecomponents/nameprefix.md)
  The portion of a name’s full form of address that precedes the name itself.
- [var givenName: String?](./personnamecomponents/givenname.md)
  Name bestowed upon an individual to differentiate them from other members of a group that share a family name.
- [var middleName: String?](./personnamecomponents/middlename.md)
  Secondary name bestowed upon an individual to differentiate them from others that have the same given name.
- [var familyName: String?](./personnamecomponents/familyname.md)
  Name bestowed upon an individual to denote membership in a group or family.
- [var nameSuffix: String?](./personnamecomponents/namesuffix.md)
  The portion of a name’s full form of address that follows the name itself.
- [var nickname: String?](./personnamecomponents/nickname.md)
  Name substituted for the purposes of familiarity.
- [var phoneticRepresentation: PersonNameComponents?](./personnamecomponents/phoneticrepresentation.md)
  The phonetic representation name components of the receiver.
### Formatting Person Name Components
- [func formatted() -> String](./personnamecomponents/formatted%28%29.md)
  Generates a locale-aware string representation of an instance of person name components using the default format style.
- [func formatted<S>(S) -> S.FormatOutput](./personnamecomponents/formatted%28_%29.md)
  Generates a locale-aware string representation of an instance of person name components using the provided format style.
- [PersonNameComponents.FormatStyle](./personnamecomponents/formatstyle.md)
  A type used to format a person’s name with a style appropriate for the given locale.
### Using Reference Types
- [class NSPersonNameComponents](./nspersonnamecomponents.md)
  An object that manages the separate parts of a person’s name to allow locale-aware formatting.
### Structures
- [PersonNameComponents.AttributedStyle](./personnamecomponents/attributedstyle.md)
- [PersonNameComponents.ParseStrategy](./personnamecomponents/parsestrategy.md)
### Initializers
- [init(String) throws](./personnamecomponents/init%28_%29.md)
  Creates a person name components object from a given string.
- [init<S>(S.ParseInput, strategy: S) throws](./personnamecomponents/init%28_,strategy%29.md)
  Creates a person name components object from a given string by applying the provided parsing strategy.
- [init(namePrefix: String?, givenName: String?, middleName: String?, familyName: String?, nameSuffix: String?, nickname: String?, phoneticRepresentation: PersonNameComponents?)](./personnamecomponents/init%28nameprefix,givenname,middlename,familyname,namesuffix,nickname,phoneticrepresentation%29.md)
### Type Aliases
- [PersonNameComponents.Specification](./personnamecomponents/specification.md)
- [PersonNameComponents.UnwrappedType](./personnamecomponents/unwrappedtype.md)
- [PersonNameComponents.ValueType](./personnamecomponents/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](./personnamecomponents/defaultresolverspecification.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomLocalizedStringResourceConvertible](./customlocalizedstringresourceconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [DisplayRepresentable](../AppIntents/displayrepresentable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [InstanceDisplayRepresentable](../AppIntents/instancedisplayrepresentable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [ReferenceConvertible](./referenceconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TypeDisplayRepresentable](../AppIntents/typedisplayrepresentable.md)

## See Also

### Names
- [class PersonNameComponentsFormatter](./personnamecomponentsformatter.md)
  A formatter that provides localized representations of the components of a person’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents)*