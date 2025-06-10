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
let rawValue: String
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

- [init(rawValue: String)](rcsmessageid/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [RCSMessageID.RawValue](rcsmessageid/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessageid/rawvalue-swift.property)*