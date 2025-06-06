# IntentCurrencyAmount

**Framework**: App Intents  
**Kind**: struct

An amount of money to transfer during a financial transaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct IntentCurrencyAmount
```

## Topics

### Creating a currency type
- [init(amount: Decimal, currencyCode: String)](intentcurrencyamount/init(amount:currencycode:).md)
  Creates a IntentCurrencyAmount from a monetary amount and a currency code.
### Getting the currency details
- [let amount: Decimal](intentcurrencyamount/amount.md)
  The monetary amount.
- [let currencyCode: String](intentcurrencyamount/currencycode.md)
  The ISO 4217 currency code that applies to the monetary amount.
### Operators
- [static func == (IntentCurrencyAmount, IntentCurrencyAmount) -> Bool](intentcurrencyamount/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intentcurrencyamount/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentcurrencyamount/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [IntentCurrencyAmount.Specification](intentcurrencyamount/specification.md)
- [IntentCurrencyAmount.UnwrappedType](intentcurrencyamount/unwrappedtype.md)
- [IntentCurrencyAmount.ValueType](intentcurrencyamount/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<IntentCurrencyAmount>](intentcurrencyamount/defaultresolverspecification.md)
### Default Implementations
- [Equatable Implementations](intentcurrencyamount/equatable-implementations.md)
- [InstanceDisplayRepresentable Implementations](intentcurrencyamount/instancedisplayrepresentable-implementations.md)
- [TypeDisplayRepresentable Implementations](intentcurrencyamount/typedisplayrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [struct IntentPaymentMethod](intentpaymentmethod.md)
  Information about a form of payment supported by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentcurrencyamount)*