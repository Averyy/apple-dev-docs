# rawValue

**Framework**: FinanceKit  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
var rawValue: Int16 { get }
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

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/creditdebitindicator/rawvalue-swift.property)*