# rawValue

**Framework**: TelephonyMessagingKit  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let rawValue: Int
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

- [init(rawValue: Int)](rcsservice/business/card/fontstyle/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [RCSService.Business.Card.FontStyle.RawValue](rcsservice/business/card/fontstyle/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/fontstyle/rawvalue-swift.property)*