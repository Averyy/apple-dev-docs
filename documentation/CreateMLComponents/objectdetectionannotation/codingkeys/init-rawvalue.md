# init(rawValue:)

**Framework**: Create ML Components  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init?(rawValue: String)
```

#### Discussion

If there is no value of the type that corresponds with the specified raw value, this initializer returns `nil`. For example:

```None
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

print(PaperSize(rawValue: "Legal"))
// Prints "Optional(PaperSize.Legal)"

print(PaperSize(rawValue: "Tabloid"))
// Prints "nil"
```

## Parameters

- `rawValue`: The raw value to use for the new instance.

## See Also

- [init?(intValue: Int)](objectdetectionannotation/codingkeys/init(intvalue:).md)
  Creates a new instance from the specified integer.
- [init?(stringValue: String)](objectdetectionannotation/codingkeys/init(stringvalue:).md)
  Creates a new instance from the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionannotation/codingkeys/init(rawvalue:))*