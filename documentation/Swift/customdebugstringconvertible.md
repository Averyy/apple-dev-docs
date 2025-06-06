# CustomDebugStringConvertible

**Framework**: Swift  
**Kind**: protocol

A type with a customized textual representation suitable for debugging purposes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol CustomDebugStringConvertible
```

#### Overview

Swift provides a default debugging textual representation for any type. That default representation is used by the `String(reflecting:)` initializer and the `debugPrint(_:)` function for types that don’t provide their own. To customize that representation, make your type conform to the `CustomDebugStringConvertible` protocol.

Because the `String(reflecting:)` initializer works for instances of  type, returning an instance’s `debugDescription` if the value passed conforms to `CustomDebugStringConvertible`, accessing a type’s `debugDescription` property directly or using `CustomDebugStringConvertible` as a generic constraint is discouraged.

> **Note**: Calling the `dump(_:_:_:_:)` function and printing in the debugger uses both `String(reflecting:)` and `Mirror(reflecting:)` to collect information about an instance. If you implement `CustomDebugStringConvertible` conformance for your custom type, you may want to consider providing a custom mirror by implementing `CustomReflectable` conformance, as well.

### Conforming to the Customdebugstringconvertible Protocol

Add `CustomDebugStringConvertible` conformance to your custom types by defining a `debugDescription` property.

For example, this custom `Point` struct uses the default representation supplied by the standard library:

```swift
struct Point {
    let x: Int, y: Int
}

let p = Point(x: 21, y: 30)
print(String(reflecting: p))
// Prints "Point(x: 21, y: 30)"
```

After adding `CustomDebugStringConvertible` conformance by implementing the `debugDescription` property, `Point` provides its own custom debugging representation.

```swift
extension Point: CustomDebugStringConvertible {
    var debugDescription: String {
        return "(\(x), \(y))"
    }
}

print(String(reflecting: p))
// Prints "(21, 30)"
```

## Topics

### Instance Properties
- [var debugDescription: String](customdebugstringconvertible/debugdescription.md)
  A textual representation of this instance, suitable for debugging.

## Relationships

### Inherited By
- [CodingKey](codingkey.md)
### Conforming Types
- [AnyHashable](anyhashable.md)
- [AnyKeyPath](anykeypath.md)
- [Array](array.md)
- [ArraySlice](arrayslice.md)
- [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md)
- [CVaListPointer](cvalistpointer.md)
- [Character](character.md)
- [ClosedRange](closedrange.md)
- [CollectionOfOne](collectionofone.md)
- [ContiguousArray](contiguousarray.md)
- [Dictionary](dictionary.md)
- [Dictionary.Keys](dictionary/keys-swift.struct.md)
- [Dictionary.Values](dictionary/values-swift.struct.md)
- [Double](double.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)
- [KeyPath](keypath.md)
- [KeyValuePairs](keyvaluepairs.md)
- [ObjectIdentifier](objectidentifier.md)
- [OpaquePointer](opaquepointer.md)
- [Optional](optional.md)
- [PartialKeyPath](partialkeypath.md)
- [Range](range.md)
- [ReferenceWritableKeyPath](referencewritablekeypath.md)
- [SIMD16](simd16.md)
- [SIMD2](simd2.md)
- [SIMD3](simd3.md)
- [SIMD32](simd32.md)
- [SIMD4](simd4.md)
- [SIMD64](simd64.md)
- [SIMD8](simd8.md)
- [Set](set.md)
- [StaticBigInt](staticbigint.md)
- [StaticString](staticstring.md)
- [String](string.md)
- [String.Index](string/index.md)
- [String.UTF16View](string/utf16view.md)
- [String.UTF8View](string/utf8view.md)
- [String.UnicodeScalarView](string/unicodescalarview.md)
- [Substring](substring.md)
- [Unicode.Scalar](unicode/scalar.md)
- [UnsafeBufferPointer](unsafebufferpointer.md)
- [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md)
- [UnsafeMutablePointer](unsafemutablepointer.md)
- [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md)
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md)
- [UnsafePointer](unsafepointer.md)
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md)
- [UnsafeRawPointer](unsaferawpointer.md)
- [WordPair](../synchronization/wordpair.md)
- [WritableKeyPath](writablekeypath.md)

## See Also

- [protocol CustomStringConvertible](customstringconvertible.md)
  A type with a customized textual representation.
- [protocol LosslessStringConvertible](losslessstringconvertible.md)
  A type that can be represented as a string in a lossless, unambiguous way.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Swift/customdebugstringconvertible)*