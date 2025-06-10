# rawValue

**Framework**: Group Activities  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- Unknown ?+ - Deprecated
- tvOS 15.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/experience-swift.enum/rawvalue-swift.property)*