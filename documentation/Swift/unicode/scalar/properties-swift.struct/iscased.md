# isCased

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the scalar is considered to be either lowercase, uppercase, or titlecase.

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
var isCased: Bool { get }
```

#### Discussion

Though similar in name, this property is  equivalent to `changesWhenCaseMapped`. The set of scalars for which `isCased` is `true` is a superset of those for which `changesWhenCaseMapped` is `true`. For example, the Latin small capitals that are used by the International Phonetic Alphabet have a case, but do not change when they are mapped to any of the other cases.

This property corresponds to the “Cased” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/iscased)*