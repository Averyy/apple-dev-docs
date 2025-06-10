# rawValue

**Framework**: Immersive Media Support  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var rawValue: String { get }
```

#### Discussion

A new instance initialized with `rawValue` will be equivalent to this instance. For example:

```None
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

let selectedSize = PaperSize.Letter
print(selectedSize.rawValue)
// Prints "Letter"

print(selectedSize == PaperSize(rawValue: selectedSize.rawValue)!)
// Prints "true"
```

## See Also

- [var intValue: Int?](fadecommand/fadetype-swift.enum/intvalue.md)
  The value to use in an integer-indexed collection (e.g. an int-keyed dictionary).
- [var stringValue: String](fadecommand/fadetype-swift.enum/stringvalue.md)
  The string to use in a named collection (e.g. a string-keyed dictionary).


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/fadetype-swift.enum/rawvalue-swift.property)*