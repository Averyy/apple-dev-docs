# Standard data types and processes

**Framework**: Technology Overviews

Store fundamental types of data, and discover the key behaviors that make using those types easier.

All apps use basic data structures to manage information. To manage simple types of data, use the types in [Swift Standard Library](../Swift/swift-standard-library.md) and the [Foundation](../Foundation/Foundation.md) framework. The types in these frameworks are often more capable than most primitive types like `int` and are also portable between Apple platforms. Use the framework types to manage:

- [Integers](../Swift/int.md), [floating-point values](../Swift/float.md) [double-precision floats](../Swift/double.md), and [Boolean](../Swift/bool.md) values
- [Strings](../Swift/string.md), [characters](../Swift/character.md), and [stylized text strings](../Foundation/attributedstring.md)
- [Dates and times](../Foundation/dates-and-times.md), and other [units of measurement](../Foundation/units-and-measurement.md)
- [Points](../Foundation/nspoint.md), [rectangles](../Foundation/nsrect.md), and other [geometric values](../Foundation/numbers-data-and-basic-values.md)
- [URLs](../Foundation/url.md) and [unique identifiers](../Foundation/uuid.md)
- [Binary data](../Foundation/data.md)
- [Arrays](../Swift/array.md), [dictionaries](../Swift/dictionary.md), [sets](../Swift/set.md), and other [collection types](../Foundation/collections.md)

The benefit of using the framework-provided types is they automatically adapt to the programming language you’re using. In Swift, types like `Int` and `Float` are actually structures you can include in collections. They also adopt standard behaviors like being [`Equatable`](../Swift/equatable.md), [`Comparable`](../Swift/comparable.md), [`Identifiable`](../Swift/identifiable.md), [`Copyable`](../Swift/copyable.md), [`Hashable`](../Swift/hashable.md), and more. You can even extend them to support custom behaviors you define.

In Objective-C, integers, floating-point values, and other primitive types map to the language’s built-in representation, but you can still use the types in object-oriented ways. For example, you can include numerical and simple types in collections by wrapping them in an [`NSNumber`](../Foundation/nsnumber.md) or [`NSValue`](../Foundation/nsvalue.md) object.

---

#### Choose the best configuration for variables

The variables you create are either *mutable* or *immutable*, meaning you can change their values after initialization or you can’t. Mutability is an important consideration when designing data structures because it impacts how you move data around your app. A structure with only immutable data values doesn’t change, so multiple tasks can safely access that structure at the same time. The same isn’t true if the structure contains a mutable value. Tasks must synchronize access to a mutable structure to avoid corrupting the data inside it.

[Swift](../Swift/Swift.md) types are inherently mutable, but you specify their actual mutability when you declare them as variables. In Swift, you declare variables using either the `let` or `var` keyword. The `let` keyword creates a variable with an immutable version of the type, and the `var` keyword creates a variable with a mutable type. The compiler enforces the mutability of variables you declare. In the following code listing, you can change the value of the `currentLoginAttempt` variable, but the compiler reports an error if you attempt to change the value in `maximumNumberOfLoginAttempts`.

```swift
let maximumNumberOfLoginAttempts = 10
var currentLoginAttempt = 0
```

In Objective-C, the mutability of a type depends on the type itself. Integers and other primitive types are inherently mutable in Objective-C unless you declare them as constants. However, the mutability of most object types depends on the type itself. The [Foundation](../Foundation/Foundation.md) framework defines mutable and immutable variants of most object types, with types being immutable unless they contain the word “mutable” in the type name. For example, the [`NSString`](../Foundation/nsstring.md) type stores an immutable string, and the [`NSMutableString`](../Foundation/nsmutablestring.md) contains the mutable version.

Choose immutable types to represent your data whenever possible. Because their values don’t change, you can pass immutable types safely around your app and access them from any task or thread. As needed, create a mutable copy of a variable to perform intermediate tasks. In Swift, copy the immutable value into a mutable variable. In Objective-C, you can create mutable versions of many immutable types using the methods of the [`NSMutableCopying`](../Foundation/nsmutablecopying.md) protocol.

---

#### Prepare to save your app’s data to disk

At some point, you’re going to want to save your app’s data to disk. The first step of this process is to convert your structured data into a serial stream of bytes that you can write to a file, which you do using the [archiving and serialization](../Foundation/archives-and-serialization.md) process. This process converts your in-memory data structures to a stream of bytes that you can then write to disk. When reading content from disk, you reverse this process by recreating your data structures from the serialized stream of bytes.

Most [Swift](../Swift/Swift.md) and [Foundation](../Foundation/Foundation.md) types have built-in support for serialization. For custom Swift types, you [add serialization support](../Foundation/encoding-and-decoding-custom-types.md), by adopting the [`Encodable`](../Swift/encodable.md) and [`Decodable`](../Swift/decodable.md) protocols. The default implementation of these protocols automatically encode and decode the properties you specify, but you can also encode and decode properties manually if you prefer.

To serialize types in Objective-C, adopt the [`NSCoding`](../Foundation/nscoding.md) and [`NSSecureCoding`](../Foundation/nssecurecoding.md) protocols to specify which properties you want to save. To generate a [`Data`](../Foundation/data.md) object with the stream of bytes from your data structure, use a [`NSKeyedArchiver`](../Foundation/nskeyedarchiver.md) object to encode one or more objects. To recreate your objects later, reverse the process using an [`NSKeyedUnarchiver`](../Foundation/nskeyedunarchiver.md) object.

---

#### Format data for different audiences

Bringing your app to other countries involves localizing text and other content to match a person’s language, but it also involves formatting data according to the person’s regional settings. Different countries and regions have rules for how to format numbers, dates, currencies, and other types of data. For example, one country might separate the fractional part of a currency using a comma, and another might use a period. Formatting data for the current [locale](../Foundation/locale.md) is one step in the [internationalization process](../Xcode/supporting-multiple-languages-in-your-app.md), which you use to make your app available globally.

Before displaying data values in your app’s interface, [format them](../Foundation/data-formatting.md) for the current region. Most Swift types have built-in methods for formatting their contents using the contents of a [`FormatStyle`](../Foundation/formatstyle.md) type. For example, apply the [`IntegerFormatStyle`](../Foundation/integerformatstyle.md) type to format a value as an integer. Format styles use the current [`Locale`](../Foundation/locale.md) and other information to format values appropriately for the current device. You can also configure format style types with custom formatting behaviors.

To format values in Objective-C, use an instance of the [`Formatter`](../Foundation/formatter.md) class to generate strings from your data. Foundation defines specific subclasses to format [dates](../Foundation/dateformatter.md), [measurable values](../Foundation/dateformatter.md) such as distances, [numbers](../Foundation/numberformatter.md), and [people’s names](../Foundation/personnamecomponentsformatter.md), among others.

---

#### Filter, sort, and compare items

Working on large amounts of data can make it difficult to organize and find that data. As the number of items in an array increases, [apply filters](../Foundation/filters-and-sorting.md) to locate the items you want. You can also [sort](../Foundation/filters-and-sorting.md) the contents of an array using rules you supply.

At the center of all filter and sort operations are *predicates*, which are logical tests to apply during the operation. A typical predicate compares a property from a data structure against a value you specify. For example, a predicate might match the name field of a structure to a name string someone specified in your interface. Build predicates in your app using the [`Predicate`](../Foundation/predicate.md) or [`NSPredicate`](../Foundation/nspredicate.md) type. You can also combine predicates to specify match multiple values. The following code uses a macro to create a [`Predicate`](../Foundation/predicate.md) structure that matches two fields of a `Message` structure against specific values.

```swift
let messagePredicate = #Predicate<Message> { message in
    message.length < 100 && message.sender == "Shelly"
}
```

Some types support the use of predicates to generate a filtered list of results. For example, the [`Array`](../Swift/array.md) type contains methods to [find elements](../Swift/array.md) using predicates. Other collection types offer similar methods.

Once you have a filtered list of results, apply sort descriptors to arrange them in a preferred order. Build a sort descriptor from the [`SortDescriptor`](../Foundation/sortdescriptor.md) or [`NSSortDescriptor`](../Foundation/nssortdescriptor.md) type, and pass them to methods of your collection types. The sort descriptors arrange elements according to the specified criteria and return a new or modified version of your collection.

---

#### Secure your data

Protect your app’s data, and store any data you write to disk securely. People’s devices contain a lot of personal information, and even information that might not seem personal can expose details about someone’s habits or choices. Apple platforms make it easy to encrypt and decrypt the data and files you create. In addition, make sure you adopt [secure policies](../Security/Security.md) for handling data to reduce the likelihood of a malicious attack gaining access to that data.

- When serializing data, adopt [secure coding](../Foundation/nssecurecoding.md) for all of your custom data types.
- [Encrypt data](../CryptoKit/CryptoKit.md) before you save it to disk, or apply [file protection attributes](../Foundation/fileprotectiontype.md) to the files you write to disk.
- Store passwords, cryptographic keys, certificates, secret information, and other small chunks of sensitive data in the device [Keychain](../Security/keychain-services.md).
- Store data files in your app’s container directory, which other apps can’t access by default.
- Validate all data you receive from external sources before incorporating it into your data structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/standard-data-types-and-processes)*