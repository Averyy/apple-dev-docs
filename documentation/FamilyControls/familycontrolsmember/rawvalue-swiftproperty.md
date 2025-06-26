# rawValue

**Framework**: FamilyControls  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
var rawValue: Int { get }
```

#### Discussion

A new instance initialized with `rawValue` will be equivalent to this instance. For example:

```swift
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

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familycontrolsmember/rawvalue-swift.property)*