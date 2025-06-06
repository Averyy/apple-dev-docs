# rawValue

**Framework**: Core HID  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var rawValue: UInt16 { get }
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidusage/fidoallianceusage/rawvalue-swift.property)*