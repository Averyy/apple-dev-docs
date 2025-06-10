# init(rawValue:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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

- [init?(intValue: Int)](fadecommand/fadetype-swift.enum/init(intvalue:).md)
  Creates a new instance from the specified integer.
- [init?(stringValue: String)](fadecommand/fadetype-swift.enum/init(stringvalue:).md)
  Creates a new instance from the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/fadetype-swift.enum/init(rawvalue:))*